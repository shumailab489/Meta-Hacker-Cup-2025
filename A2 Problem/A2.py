import os

def can_with_h(heights, h):
    """Return True if with ladder height h all platforms are reachable from ground."""
    n = len(heights)
    if n == 0:
        return True
    # Walk through platforms, splitting where adjacent difference > h
    i = 0
    while i < n:
        # start of component at i
        comp_min = heights[i]
        j = i
        while j + 1 < n and abs(heights[j+1] - heights[j]) <= h:
            j += 1
            if heights[j] < comp_min:
                comp_min = heights[j]
        # component is [i..j], check if it has a platform with height <= h
        if comp_min > h:
            return False
        # continue after the component
        i = j + 1
    return True

def solve_file(input_path, output_path):
    with open(input_path, 'r') as fin:
        t_line = fin.readline()
        if not t_line:
            raise ValueError("Empty input file or missing T")
        T = int(t_line.strip())
        results = []
        for case in range(1, T+1):
            n_line = fin.readline()
            while n_line is not None and n_line.strip() == "":
                # skip blank lines (robustness)
                n_line = fin.readline()
            if not n_line:
                raise ValueError(f"Unexpected EOF when reading N for case {case}")
            n = int(n_line.strip())
            a_line = fin.readline()
            while a_line is not None and a_line.strip() == "":
                a_line = fin.readline()
            if not a_line:
                raise ValueError(f"Unexpected EOF when reading array for case {case}")
            A = list(map(int, a_line.strip().split()))
            if len(A) != n:
                # allow if input wraps lines (try to read more)
                while len(A) < n:
                    extra = fin.readline()
                    if not extra:
                        break
                    A.extend(map(int, extra.strip().split()))
                if len(A) != n:
                    raise ValueError(f"Expected {n} numbers for case {case}, found {len(A)}")
            # binary search h in [0, max(A)]
            lo, hi = 0, max(A) if A else 0
            while lo < hi:
                mid = (lo + hi) // 2
                if can_with_h(A, mid):
                    hi = mid
                else:
                    lo = mid + 1
            results.append(f"Case #{case}: {lo}")
    with open(output_path, 'w') as fout:
        fout.write("\n".join(results))

if __name__ == "__main__":
    base_path = r"C:\Users\Abbas Buzdar\Desktop\Meta Hacker Cup"
    input_file = os.path.join(base_path, "snake_scales_chapter_2_input.txt")
    output_file = os.path.join(base_path, "snake_scales_chapter_2_output.txt")
    solve_file(input_file, output_file)
    print(f"✅ Output written to: {output_file}")

