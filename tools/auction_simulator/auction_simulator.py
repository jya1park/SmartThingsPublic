#!/usr/bin/env python3
"""Simple foreclosure auction simulator for Hwaseong-si properties.

This module contains a small dataset with fictional apartment and detached house
listings. It provides a command line interface that can list available items and
simulate how the proceeds from a predicted winning bid would be distributed
according to lien priority on the auction decision date.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from typing import Iterable, List, Optional


@dataclass(frozen=True)
class Lien:
    """Represents a secured claim that participates in the auction proceeds."""

    ranking: int
    creditor: str
    amount: int  # Stored in Korean won


@dataclass(frozen=True)
class Property:
    """Represents a property that can appear in an auction catalog."""

    property_id: str
    name: str
    property_type: str  # "apartment" or "house"
    address: str
    appraised_value: int
    starting_bid: int
    size_m2: float
    description: str
    liens: List[Lien] = field(default_factory=list)

    def format_summary(self) -> str:
        """Render a human friendly summary of the property."""
        return (
            f"[{self.property_id}] {self.name}\n"
            f"  유형: {self.property_type}\n"
            f"  소재지: {self.address}\n"
            f"  감정가: {self.appraised_value:,}원\n"
            f"  최저매각가: {self.starting_bid:,}원\n"
            f"  전용면적: {self.size_m2:.1f}㎡\n"
            f"  비고: {self.description}\n"
        )


PROPERTIES: List[Property] = [
    Property(
        property_id="APT-001",
        name="동탄역 센트럴파크 서희스타힐스 84㎡",
        property_type="apartment",
        address="경기도 화성시 오산동 868",
        appraised_value=520_000_000,
        starting_bid=364_000_000,
        size_m2=84.9,
        description="동탄역 도보권, 생활편의시설 우수",
        liens=[
            Lien(ranking=1, creditor="국민은행 근저당", amount=280_000_000),
            Lien(ranking=2, creditor="화성시 세무과 체납세", amount=8_000_000),
            Lien(ranking=3, creditor="관리사무소 관리비", amount=3_200_000),
        ],
    ),
    Property(
        property_id="APT-002",
        name="동탄 레이크자이 101㎡",
        property_type="apartment",
        address="경기도 화성시 청계동 533",
        appraised_value=690_000_000,
        starting_bid=483_000_000,
        size_m2=101.4,
        description="호수공원 인접, 학군 양호",
        liens=[
            Lien(ranking=1, creditor="신한은행 근저당", amount=360_000_000),
            Lien(ranking=2, creditor="중앙하이츠 전세보증금", amount=120_000_000),
            Lien(ranking=3, creditor="관리사무소 관리비", amount=2_800_000),
        ],
    ),
    Property(
        property_id="HOU-001",
        name="향남읍 단독주택 125㎡",
        property_type="house",
        address="경기도 화성시 향남읍 한내리 312-5",
        appraised_value=410_000_000,
        starting_bid=287_000_000,
        size_m2=125.6,
        description="향남제약단지 인근, 단독주택",
        liens=[
            Lien(ranking=1, creditor="기업은행 근저당", amount=220_000_000),
            Lien(ranking=2, creditor="주택도시보증공사 전세금", amount=95_000_000),
            Lien(ranking=3, creditor="화성시 재산세", amount=4_500_000),
        ],
    ),
    Property(
        property_id="HOU-002",
        name="봉담읍 다가구주택 198㎡",
        property_type="house",
        address="경기도 화성시 봉담읍 동화리 89-12",
        appraised_value=530_000_000,
        starting_bid=371_000_000,
        size_m2=198.2,
        description="봉담2신도시 생활권, 다가구",
        liens=[
            Lien(ranking=1, creditor="우리은행 근저당", amount=310_000_000),
            Lien(ranking=2, creditor="임차인 보증금", amount=150_000_000),
            Lien(ranking=3, creditor="관리비", amount=5_600_000),
        ],
    ),
]


def get_properties(property_type: Optional[str] = None) -> Iterable[Property]:
    """Yield properties, optionally filtered by type."""
    for prop in PROPERTIES:
        if property_type and prop.property_type != property_type:
            continue
        yield prop


def find_property(property_id: str) -> Optional[Property]:
    """Return a property from the catalog if it exists."""
    for prop in PROPERTIES:
        if prop.property_id.upper() == property_id.upper():
            return prop
    return None


def simulate_distribution(prop: Property, expected_price: int) -> str:
    """Simulate how the winning bid would be distributed among liens."""
    lines: List[str] = []
    remaining = expected_price

    lines.append(
        f"예상 낙찰가 {expected_price:,}원 기준 배당 시뮬레이션 (감정가 {prop.appraised_value:,}원, 최저매각가 {prop.starting_bid:,}원)"
    )

    for lien in sorted(prop.liens, key=lambda x: x.ranking):
        if remaining <= 0:
            lines.append(
                f"- {lien.ranking}순위 {lien.creditor}: 배당 없음 (잔여금액 부족)"
            )
            continue

        payout = min(lien.amount, remaining)
        remaining -= payout
        satisfaction = "전액 배당" if payout == lien.amount else "부분 배당"
        lines.append(
            f"- {lien.ranking}순위 {lien.creditor}: {payout:,}원 배당 ({satisfaction})"
        )

    if remaining > 0:
        lines.append(
            f"- 잔여금: {remaining:,}원 (후순위 채권자 또는 소유자에게 환급)"
        )
    else:
        lines.append("- 잔여금: 0원")

    highest_priority = min(prop.liens, key=lambda x: x.ranking)
    priority_status = (
        "전액 회수"
        if expected_price >= highest_priority.amount
        else "부분 회수"
    )
    lines.append(
        f"최우선순위({highest_priority.creditor})는 {priority_status} 상태입니다."
    )

    return "\n".join(lines)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list", help="List available properties")
    list_parser.add_argument(
        "--type",
        choices={"apartment", "house"},
        help="Filter by property type",
    )

    simulate_parser = subparsers.add_parser(
        "simulate", help="Simulate lien distribution for a property"
    )
    simulate_parser.add_argument("property_id", help="ID of the property to simulate")
    simulate_parser.add_argument(
        "--price",
        type=int,
        required=True,
        help="Expected winning bid (Korean won)",
    )

    return parser


def handle_list_command(property_type: Optional[str]) -> None:
    props = list(get_properties(property_type))
    if not props:
        print("해당 유형의 물건이 존재하지 않습니다.")
        return

    for prop in props:
        print(prop.format_summary())


def handle_simulate_command(property_id: str, price: int) -> None:
    prop = find_property(property_id)
    if not prop:
        print(f"ID가 {property_id!r}인 물건을 찾을 수 없습니다.")
        return

    result = simulate_distribution(prop, price)
    print(result)


def main(argv: Optional[Iterable[str]] = None) -> None:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    if args.command == "list":
        handle_list_command(args.type)
    elif args.command == "simulate":
        handle_simulate_command(args.property_id, args.price)
    else:
        parser.print_help()


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    main()
