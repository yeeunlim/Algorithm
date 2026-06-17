def solution(today, terms, privacies):
    def to_days(date):
        y, m, d = map(int, date.split('.'))
        days = y * (12 * 28) + (m - 1) * 28 + (d - 1)
        return days
    
    # {약관 종류: 유효기간}
    # 예: {'A': 140, 'B': 308, 'C': 56}
    terms_dict = {}
    for term in terms:
        term_type, months = term.split()
        months_days = int(months) * 28
        terms_dict[term_type] = months_days
        
    # {개인정보 번호: 만료일}
    # 예: {1: 679309, 2: 679532, 3: 679494, 4: 679495}
    privacies_dict = {}
    for i, privacy in enumerate(privacies):
        # 2021.05.02, A
        collect_date, term_type = privacy.split()
        collect_date = to_days(collect_date)
        # 만료일 = 수집일 + 유효기간
        expire_date = collect_date + terms_dict[term_type]
        privacies_dict[i + 1] = expire_date
        
    # 만료일 - 오늘 날짜 < 0 -> 파기
    # 파기 개인정보 번호(1~n) 반환
    answer = [key for key in privacies_dict.keys() if privacies_dict[key] - to_days(today) <= 0]
    return answer