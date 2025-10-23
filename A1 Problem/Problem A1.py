import os

def shortest_ladder_height(heights):
    # If only one platform, no ladder is needed
    if len(heights) <= 1:
        return 0
    # Otherwise, find the maximum vertical difference
    return max(abs(heights[i+1] - heights[i]) for i in range(len(heights) - 1))

def solve(input_file, output_file):
    with open(input_file, 'r') as f:
        t = int(f.readline().strip())
        results = []
        for case_num in range(1, t + 1):
            n = int(f.readline().strip())
            A = list(map(int, f.readline().strip().split()))
            result = shortest_ladder_height(A)
            results.append(f"Case #{case_num}: {result}")
    
    with open(output_file, 'w') as f:
        f.write("\n".join(results))

# ✅ File paths (make sure these exist)
base_path = r"C:\Users\Abbas Buzdar\Desktop\Meta Hacker Cup"
input_file = os.path.join(base_path, "snake_scales_chapter_1_input.txt")
output_file = os.path.join(base_path, "snake_scales_chapter_1_output.txt")

# Run the solution
solve(input_file, output_file)

print(f"✅ Output successfully saved to:\n{output_file}")

