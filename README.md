# 프로토콜 프로그래밍 예제

    https://yoonkh.github.io/python/2017/12/10/brain4.html
    에 있는 예제를 따라 적으면서 공부하는 repo.

    서버/클라이언트 공용 모듈 + 서버 + 클라이언트로 구성 될 것.

    파일 업로드 프로토콜을 구현 할 것 이다. 헤더와 바디 두 부분으로 나누고
    바디에는 실제 전달하고자 하는 데이터, 헤더는 본문 길이 및 메세지 메타데이터 몇가지를 포함.

    헤더의 길이는 16바이트로 일정하게 유지. 따라서 데이터를 받았을때 첫 16바이트를 분석하고, 메시지 길이를 확인해서 메시지 끝을 끊어 낸다.
    
# Bluetooth Python (with MAC OSX 10.15.x)
    일반적인 PyBluez를 install 하면 무조건 import 과정에서 에러가 발생한다.
    MAC OSX 10.15.xx를 사용하는 사람은, 가상환경에 Python3.7.x 버전을 준비하고.
    https://github.com/tigerking/pybluez/releases 
    위 링크에 있는 PyBluez-0.30-cp37-cp37m-macosx_10_13_x86_64.whl 를 다운로드 받아서
    `python3 -m pip install <PATH/PyBluez-0.30-cp37-cp37m-macosx_10_13_x86_64.whl>` 로 인스톨 해야 한다. 
    공식 문서에는 다음과 같이 설치하라고 나온다.
    pip uninstall pybluez
    pip install git+https://github.com/pybluez/pybluez.git 
    이 경우 discover_devices() 함수는 정상적으로 실행 되지만 ,
    advertise_service() 함수 실행 과정에서 MAC OSX 의 특성으로 인한 오류가 발생한다.
    꼭 tigerking 유저의 customed 버전을 사용해야 한다(MACOS 10.15.x 버전 사용자라면)
    추가적으로 설치 과정에서 xcode를 이용한 build 과정이 포함 되어 있으므로.
    `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer` 를 이용해서 빌드 & 설치 한 뒤
    `sudo xcode-select --switch /Library/Developer/CommandLineTools` 로 원상 복구하면 되겠다.

# MAC OSX 10.15.xx gattlib issue
    MAC OS에서는 BLE 통신을 위한 패키지인 gattlib 설치가 불가능 하다.
    여러 방면으로 찾아 봤으나 지원이 안된다고 함. 
    따라서 대안으로 bluepy 라는 패키지 고려 중.
    https://github.com/IanHarvey/bluepy