from app import answer_question

test_cases = [
    {
        "question": "What is FAISS used for?",
        "expected_keywords": ["similarity search", "clustering", "vectors"]
    },
    {
        "question": "What is Python known for?",
        "expected_keywords": ["readability", "versatility"]
    },
    {
        "question": "What is deep learning?",
        "expected_keywords": ["neural networks", "layers"]
    },
]

def run_tests():
    passed = 0
    total = len(test_cases)

    for i, test in enumerate(test_cases, start=1):
        answer, _ = answer_question(test["question"])
        answer_lower = answer.lower()
        matched = [kw for kw in test["expected_keywords"] if kw.lower() in answer_lower]
        score = len(matched) / len(test["expected_keywords"])
        result = "PASS" if score >= 0.5 else "FAIL"

        print(f"Test {i}: {result}")
        print(f"  Question: {test['question']}")
        print(f"  Answer: {answer}")
        print(f"  Score: {score*100:.0f}%\n")

        if result == "PASS":
            passed += 1

    print(f"Total: {passed}/{total} tests passed ({passed/total*100:.0f}%)")

if __name__ == "__main__":
    run_tests()