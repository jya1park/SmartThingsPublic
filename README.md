# SmartThings Public GitHub Repo

An official list of SmartApps and Device Types from SmartThings.

Here are some links to help you get started coding right away:

* [GitHub-specific Documentation](http://docs.smartthings.com/en/latest/tools-and-ide/github-integration.html)
* [Full Documentation](http://docs.smartthings.com)
* [IDE & Simulator](http://ide.smartthings.com)
* [Community Forums](http://community.smartthings.com)

Follow us on the web:

* Twitter: http://twitter.com/smartthingsdev
* Facebook: http://facebook.com/smartthingsdevelopers

스마트폰 센서 데이터와 딥러닝 기반 실내 위치 추적 및 경로 재구성 기술 
(Indoor Positioning and Path Reconstruction Technology Based on Smartphone Sensor Data and Deep Learning)
1. 특허의 배경
1-1. 본 발명의 기술분야
본 발명은 실내 위치 추적 기술 분야에 속하며, 특히 스마트폰 센서 데이터, 건물 평면도, 그리고 지자기 센서 데이터를 활용하여 실내에서 보행자의 위치를 정밀하게 파악하는 기술에 관한 것이다. 이 기술은 스마트 빌딩, 보안 시스템, 실내 내비게이션 서비스 등 다양한 분야에서 필수적인 정확한 실내 위치 추적 시스템의 필요성을 해결하기 위해 개발되었다.

1-2. 기존 기술의 설명
기존의 실내 위치 추적 기술은 주로 Wi-Fi와 **Bluetooth Low Energy (BLE)**와 같은 무선 신호를 기반으로 한다. 이러한 방법은 널리 사용되고 있지만, 특히 멀티패스 효과로 인해 위치 정확도가 크게 저하되는 문제가 있다. 멀티패스 효과는 신호가 벽이나 천장 등 물체에 반사되어 여러 경로로 수신되면서 발생하는 현상으로, 이로 인해 실제 위치와 다른 위치가 감지될 수 있다.
반면, Fingerprint 기반 매핑은 더 높은 정확도를 제공하는 대안으로 주목받고 있다. 이 방법은 특정 지점에서 수집된 센서 데이터(예: 가속도계, 자이로스코프)를 기반으로 상세한 지도를 생성한다. 실시간으로 수집된 센서 데이터를 미리 구축된 Fingerprint 데이터와 비교하여 사용자의 위치를 정확하게 파악할 수 있다. 그러나 Fingerprint 매핑은 높은 정확도를 제공함에도 불구하고 몇 가지 중요한 문제점이 존재한다.
1-3. 존재하는 기술의 문제점
Fingerprint 매핑은 다음과 같은 주요 문제점에 직면해 있다:
1.	환경 변화에 대한 민감도: Fingerprint 지도는 물리적 환경 변화에 매우 민감하다. 예를 들어, 가구 배치 변경, 건설 활동, 또는 보행자 흐름의 변화 등은 센서 데이터를 변경시켜 Fingerprint 지도를 구식으로 만들 수 있다.
2.	시간적 변동성: 시간이 지남에 따라 특정 지점에서 수집된 센서 데이터는 스마트폰 하드웨어의 변화나 센서 보정 오차로 인해 변할 수 있다.
3.	공간적 한계: 건물 내 다양한 구역에서 Fingerprint 매핑의 정확도가 크게 달라질 수 있으며, 특히 복잡한 구조나 다층 건물에서는 이 문제가 더욱 두드러진다.
이러한 문제들은 환경 변화에 적응할 수 있는 강력한 솔루션의 필요성을 강조한다.

1-4. 특허의 목적
본 발명은 위와 같은 문제점을 해결하기 위해 고급 알고리즘과 데이터 융합 기술을 활용한 Fingerprint 지도 업데이트 방법을 제안한다. 구체적으로, 본 발명은 다음과 같은 목적을 달성하고자 한다:
1.	PDR 한계 극복: 딥러닝을 활용하여 사용자의 행동 패턴과 무관하게 보행자의 이동 경로를 정확하게 추정함으로써 기존 Pedestrian Dead Reckoning (PDR) 시스템의 한계를 극복한다.
2.	데이터 융합 강화: 보행자 이동 중 수집된 스마트폰 센서 데이터와 지자기 센서 데이터를 효과적으로 통합하여 정확한 위치 추적 및 PDR의 방향을 예측한다..
3.	자기장 Fingerprint 없이 경로 재구성: 획득한 경로, 시작점 위치, 방향 정보와 지도 정보를 활용하여 자기장 Fingerprint 데이터 없이도 소비자 경로를 재구성한다.
4.	자기장 Fingerprint 업데이트: 재구성한 경로를 기반으로 자기장 Fingerprint 정보를 지속적으로 업데이트하여 Fingerprint Map 정확도를 유지한다.

이러한 목적을 달성함으로써 본 발명은 실내 위치 추적 시스템의 정확성과 신뢰성을 향상시킬 뿐만 아니라, 동적 환경에 적응할 수 있는 능력을 제공하여 실내 내비게이션 기술의 중요한 발전을 이끌어낸다.

2. 발명의 구체적 설명
2-1. 발명의 구성
본 발명은 크게 데이터 취득 모듈, 경로 변환 모듈, 실시간 위치 추정 모듈, 그리고 Fingerprint Map 업데이트 모듈 로 구성된다.
