"""
버블 정렬(Bubble Sort) 구현 예제

함수 `bubble_sort`는 입력 시퀀스를 정렬된 리스트로 반환합니다.
- 기본은 오름차순
- `reverse=True`로 내림차순
- `in_place=True`로 입력 리스트를 직접 정렬할 수 있습니다.

간단한 데모와 기본 검증(assert)가 `__main__`에 포함되어 있습니다.
"""
from __future__ import annotations

from typing import Iterable, List, Sequence
import time


def bubble_sort(seq: Sequence, *, reverse: bool = False, in_place: bool = False) -> List:
	"""Bubble sort implementation.

	Args:
		seq: 정렬할 수 있는 시퀀스(예: 리스트, 튜플).
		reverse: True면 내림차순으로 정렬.
		in_place: True면 전달된 리스트를 직접 수정하고 동일 객체를 반환.

	Returns:
		정렬된 리스트 객체.

	Notes:
		이 구현은 안정적이며, 최적화로 교환이 없을 경우 반복을 조기 종료합니다.
	"""
	if in_place:
		lst = seq  # type: ignore
	else:
		lst = list(seq)

	n = len(lst)
	if n <= 1:
		return lst  # 바로 반환

	for i in range(n):
		swapped = False
		# 마지막 i개는 이미 정렬되어 있음
		for j in range(0, n - i - 1):
			a, b = lst[j], lst[j + 1]
			should_swap = (a > b) if not reverse else (a < b)
			if should_swap:
				lst[j], lst[j + 1] = b, a
				swapped = True
		if not swapped:
			break

	return lst


def _demo() -> None:
	sample = [64, 34, 25, 12, 22, 11, 90]
	print("원본:", sample)

	asc = bubble_sort(sample)
	print("오름차순:", asc)

	desc = bubble_sort(sample, reverse=True)
	print("내림차순:", desc)

	# in_place 예제
	inplace_list = sample.copy()
	bubble_sort(inplace_list, in_place=True)
	print("in_place 정렬 결과:", inplace_list)


if __name__ == "__main__":
	# 간단한 동작 검증
	assert bubble_sort([3, 2, 1]) == [1, 2, 3]
	assert bubble_sort([1, 2, 3], reverse=True) == [3, 2, 1]

	print("버블 정렬 데모 실행")
	start = time.perf_counter()
	_demo()
	end = time.perf_counter()
	print(f"데모 실행 시간: {end - start:.6f}초")

