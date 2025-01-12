import os
from difflib import SequenceMatcher

def calculate_similarity(content1, content2):
    """
    Calculate the similarity ratio between two strings using SequenceMatcher.

    Args:
        content1 (str): Content of the first file.
        content2 (str): Content of the second file.
    
    Returns:
        float: Similarity ratio between 0 and 1.
    """
    return SequenceMatcher(None, content1, content2).ratio()

def find_similar_files(folder_path, threshold=0.3):
    """
    Find and list files in a folder that are more than a given percentage similar.

    Args:
        folder_path (str): Path to the folder containing files.
        threshold (float): Similarity threshold (e.g., 0.3 for 30% similarity).
    
    Returns:
        dict: A dictionary where the key is the file name and the value is a list of files with similar content.
    """
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    similar_files = {}

    for i, file1 in enumerate(files):
        file1_path = os.path.join(folder_path, file1)
        with open(file1_path, 'r') as f1:
            content1 = f1.read()

        for j, file2 in enumerate(files):
            if i >= j:  # Avoid redundant comparisons and self-comparisons
                continue

            file2_path = os.path.join(folder_path, file2)
            with open(file2_path, 'r') as f2:
                content2 = f2.read()

            # Calculate similarity
            similarity = calculate_similarity(content1, content2)
            if similarity > threshold:
                if file1 not in similar_files:
                    similar_files[file1] = []
                similar_files[file1].append((file2, round(similarity * 100, 2)))

    return similar_files


if __name__ == "__main__":
    folder = "C:\\Users\\Administrator\\Desktop\\python program\\palagrizumcheacker"  # Replace with the path to your folder

    if os.path.exists(folder) and os.path.isdir(folder):
        threshold = 0.3  # 30% similarity threshold
        similar_files = find_similar_files(folder, threshold)
        if similar_files:
            print(f"Files with more than {threshold * 100}% similarity:")
            for file, matches in similar_files.items():
                print(f"{file} is similar to:")
                for match in matches:
                    print(f"  - {match[0]} ({match[1]}% similarity)")
        else:
            print(f"No files with more than {threshold * 100}% similarity found.")
    else:
        print("Invalid folder path.")
