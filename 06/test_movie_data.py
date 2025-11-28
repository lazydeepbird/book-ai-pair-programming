"""
movie.py 클래스를 위한 테스트 데이터 모음
"""

from datetime import datetime, timedelta
from movie import Movie, Ticket

# ===== Movie 테스트 데이터 =====
# 영화 객체 생성 테스트
movie1 = Movie("아바타: 물의 길")
movie2 = Movie("오펜하이머")
movie3 = Movie("바비")
movie4 = Movie("인사이드 아웃 2")
movie5 = Movie("미션 임파서블: 데드 레코닝")

# 영화 목록
movies = [movie1, movie2, movie3, movie4, movie5]

print("=" * 50)
print("📽️  생성된 영화 데이터")
print("=" * 50)
for idx, movie in enumerate(movies, 1):
    print(f"{idx}. 제목: {movie.title}")
    print(f"   ID: {movie.id}")
    print()

# ===== Ticket 테스트 데이터 =====
# 현재 시간 기준 예매 시간 생성
base_time = datetime.now()
ticket_times = [
    base_time + timedelta(days=0, hours=14, minutes=0),   # 오늘 14:00
    base_time + timedelta(days=0, hours=16, minutes=30),  # 오늘 16:30
    base_time + timedelta(days=1, hours=10, minutes=0),   # 내일 10:00
    base_time + timedelta(days=1, hours=19, minutes=0),   # 내일 19:00
    base_time + timedelta(days=2, hours=15, minutes=30),  # 모레 15:30
]

# 티켓 객체 생성
tickets = []
for i, (movie, time) in enumerate(zip(movies, ticket_times)):
    ticket = Ticket(movie, time)
    tickets.append(ticket)

print("=" * 50)
print("🎫 생성된 티켓 데이터")
print("=" * 50)
for idx, ticket in enumerate(tickets, 1):
    print(f"{idx}. 티켓 ID: {ticket.id}")
    print(f"   영화 ID: {ticket.movie_id}")
    print(f"   예매 시간: {ticket.time.strftime('%Y-%m-%d %H:%M')}")
    print()

# ===== 테스트 케이스 =====
print("=" * 50)
print("✅ 테스트 케이스")
print("=" * 50)

# 테스트 1: 영화 객체 생성 확인
print("Test 1: 영화 객체 생성 확인")
assert isinstance(movie1, Movie), "Movie 객체 생성 실패"
assert movie1.title == "아바타: 물의 길", "제목 설정 실패"
assert movie1.id is not None, "ID 생성 실패"
print("✓ 통과: 영화 객체 정상 생성")
print()

# 테스트 2: 각 영화의 ID가 고유한지 확인
print("Test 2: 영화 ID 고유성 확인")
movie_ids = [movie.id for movie in movies]
assert len(movie_ids) == len(set(movie_ids)), "중복된 ID 존재"
print("✓ 통과: 모든 영화의 ID가 고유함")
print()

# 테스트 3: 티켓 객체 생성 확인
print("Test 3: 티켓 객체 생성 확인")
assert isinstance(tickets[0], Ticket), "Ticket 객체 생성 실패"
assert tickets[0].movie_id == movie1.id, "영화 ID 매핑 실패"
assert tickets[0].time == ticket_times[0], "시간 설정 실패"
print("✓ 통과: 티켓 객체 정상 생성")
print()

# 테스트 4: 각 티켓의 ID가 고유한지 확인
print("Test 4: 티켓 ID 고유성 확인")
ticket_ids = [ticket.id for ticket in tickets]
assert len(ticket_ids) == len(set(ticket_ids)), "중복된 티켓 ID 존재"
print("✓ 통과: 모든 티켓의 ID가 고유함")
print()

# 테스트 5: 티켓의 영화 ID가 올바른지 확인
print("Test 5: 티켓-영화 연관성 확인")
for ticket, movie in zip(tickets, movies):
    assert ticket.movie_id == movie.id, f"티켓의 영화 ID가 일치하지 않음"
print("✓ 통과: 모든 티켓이 올바른 영화와 연결됨")
print()

print("=" * 50)
print("✅ 모든 테스트 통과!")
print("=" * 50)
