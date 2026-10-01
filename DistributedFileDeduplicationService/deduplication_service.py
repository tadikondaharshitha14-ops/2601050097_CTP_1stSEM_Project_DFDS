from duplicate_detector import DuplicateDetector


class DeduplicationService:

    def run(self, folder):

        detector = DuplicateDetector()

        duplicates = detector.find_duplicates(folder)

        print("\nDeduplication Report")
        print("--------------------")

        if duplicates:
            print("Duplicate files:")
            for file in duplicates:
                print(file)
        else:
            print("No duplicate files found.")


service = DeduplicationService()

service.run("storage")