from pathlib import Path


class ChangeDetector:


    def compare(self, path):


        root = Path(path)


        result = {

            "added": [],

            "modified": [],

            "removed": []

        }


        if not root.exists():

            return result


        for file in root.rglob("*"):


            if file.is_file():


                relative = str(
                    file.relative_to(root)
                )


                # نسخه اولیه:
                # ثبت فایل‌های موجود
                # آماده اتصال به Git diff


                result["modified"].append(
                    relative
                )


        return result




changes = ChangeDetector()
