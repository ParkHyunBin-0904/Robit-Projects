import requests

def get_weather():
    # 오픈 API를 사용해 서울의 현재 날씨 데이터를 가져옵니다.
    # WTTR.in은 인증키가 필요 없는 무료 날씨 API 서비스입니다.
    url = "https://wttr.in/Seoul?format=j1"
    
    print("🌐 서울 실시간 날씨 정보를 가져오는 중...")
    
    try:
        # 1. requests.get() 메소드를 이용해 웹에 데이터를 요청합니다.
        response = requests.get(url)
        
        # HTTP 상태 코드가 200(성공)이 아니면 에러를 발생시킵니다.
        response.raise_for_status()
        
        # 2. 받아온 JSON 형식의 응답 데이터를 파이썬 딕셔너리로 변환합니다.
        data = response.json()
        
        # 3. 데이터 구조 분석 후 필요한 정보 파싱
        current = data['current_condition'][0]
        temp = current['temp_C']           # 현재 기온
        feel_like = current['FeelsLikeC']  # 체감 기온
        weather_desc = current['weatherDesc'][0]['value']  # 날씨 상태 설명
        humidity = current['humidity']     # 습도
        
        # 4. 결과 출력
        print("\n==============================")
        print("☀️  오늘의 서울 실시간 날씨 보고서  ☀️")
        print("==============================")
        print(f"🌡️  현재 기온: {temp}°C (체감 기온: {feel_like}°C)")
        print(f"☁️  날씨 상태: {weather_desc}")
        print(f"💧  현재 습도: {humidity}%")
        print("==============================")
        
    except requests.exceptions.HTTPError as http_err:
        print(f" HTTP 에러 발생: {http_err}")
    except requests.exceptions.ConnectionError:
        print(" 네트워크 연결 에러! 인터넷 연결을 확인해 주세요.")
    except Exception as err:
        print(f" 예상치 못한 오류 발생: {err}")

if __name__ == "__main__":   
    # __name__은 파이썬이 내부적으로 사용하는 특별한 변수입니다.
    # 이 파일(main.py)이 직접 실행될 경우 __name__ 변수에는 "__main__"이 대입됩니다.
    # 따라서, 이 조건문은 "이 파일이 프로그램의 시작점(Entry Point)으로 직접 실행될 때만" 작동합니다.
    get_weather()
