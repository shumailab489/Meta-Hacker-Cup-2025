import os

def build_sequence(N, A, B):
    # Find a divisor d of B with d <= A (choose the largest such for smaller B/d)
    d = 1
    # iterate down from min(A, B) to 1 to get largest divisor <= A
    for cand in range(min(A, B), 0, -1):
        if B % cand == 0:
            d = cand
            break
    # First half: N-1 ones, then d
    first_half = [1] * (N - 1) + [d]
    # Second half: N-1 ones, then B//d
    second_half = [1] * (N - 1) + [B // d]
    return first_half + second_half

def solve_file(input_path, output_path):
    with open(input_path, 'r') as fin:
        t_line = fin.readline()
        if not t_line:
            raise ValueError("Empty input file or missing T")
        T = int(t_line.strip())
        out_lines = []
        for case in range(1, T + 1):
            line = fin.readline()
            while line is not None and line.strip() == "":
                line = fin.readline()
            if not line:
                raise ValueError(f"Unexpected EOF when reading case {case}")
            N, A, B = map(int, line.strip().split())
            seq = build_sequence(N, A, B)
            out_lines.append(f"Case #{case}: " + " ".join(map(str, seq)))
    with open(output_path, 'w') as fout:
        fout.write("\n".join(out_lines))

if __name__ == "__main__":
    base_path = r"C:\Users\Abbas Buzdar\Desktop\Meta Hacker Cup"
    input_file = os.path.join(base_path, "final_product_chapter_1_input.txt")
    output_file = os.path.join(base_path, "final_product_chapter_1_output.txt")
    solve_file(input_file, output_file)
    print(f"✅ Output written to: {output_file}")

