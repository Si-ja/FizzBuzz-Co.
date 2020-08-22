class FizzBuzz:
    """
    FizzBuzz is a class that allows to not only complete the FizzBuzz challenge with one line of
    code. But also allows to test the answers of the individual user.
    """

    def __init__(self,
                 fizz=3,
                 buzz=5,
                 failure_msg = "The candidate has not passed.",
                 success_msg = "The candidate has passed."):
        self.fizz=fizz
        self.buzz=buzz
        self.failure_msg=failure_msg
        self.success_msg=success_msg

    def fizzbuzz(self, amount, start=1):
        """
        This method allows to print out values in respect to fizzbuzz criteria.
        :param amount: Amount of values that need to be printed out.
        :param start: The starting point from which value FizzBuzz expression should be built.
                      It should not be 0 or a negative value. Defaults: 1.
        :return: Void. Every single value of FizzBuzz in the range (start, amount+start) are
                 printed out on a new line.
        """
        if amount < 1:
            raise ValueError("There cannot be 0 values or less")
        if type(amount) != int:
            raise ValueError("A number of values needs to be an integer value")
        if type(start) != int:
            raise ValueError("The starting point needs to be defined with an integer value")
        for i in range(start, start + amount):
            answer = ""
            if i % self.fizz == 0: answer += "Fizz"
            if i % self.buzz == 0: answer += "Buzz"
            if answer == "": answer = i
            print(answer)

    def compliance(self, sequence, start=1) -> str:
        """
        This method allows to check whether the candidate's answer match the requirements
        of FizzBuzz task. Essentially, it is like a unit test for candidate's performance.
        :param sequence: This should be the sequence of candidates' answers presented in a list.
        :param start: The starting point, from which it is taken the candidate is generatinig FizzBuzz sequence.
                      Defaults to 1.
        :return: A message informing the recruiter if the candidate has passed or failed the excercise.
        """
        if type(sequence) != list or not sequence:
            raise ValueError("Data input is either missing or not in a list.")
        if type(start) != int:
            raise ValueError("The starting point needs to be an integer value.")
        grade = ""
        for i in sequence:
            answer = ""
            if start % self.fizz == 0: answer += "Fizz"
            if start % self.buzz == 0: answer += "Buzz"
            if answer == "": answer = start
            if answer != i:
                grade = self.failure_msg
                return grade
            start += 1
        grade = self.success_msg
        return grade

    def compliance_report(self, sequence, start):
        """
        This method allows to check whether the candidate's answer match the requirements
        of FizzBuzz task. Essentially, it is like a unit test for candidate's performance.
        However, additionally, it generate a report on what the candidate got correct and wrong,
        which is saved in a Markdown file for tracking.
        :param sequence: his should be the sequence of candidates' answers presented in a list.
        :param start: The starting point, from which it is taken the candidate is generatinig FizzBuzz sequence.
                      Defaults to 1.
        :return: Void. A report with the current date and time is saved to allow for easier tracking
                 of candidates performance.
        """
        from datetime import datetime
        if type(sequence) != list or not sequence:
            raise ValueError("Data input is either missing or not in a list.")
        if type(start) != int:
            raise ValueError("The starting point needs to be an integer value.")
        txt_answer = "Real Answer | Candidate's Answer | Status\n" \
                 ":------------: | :------------: | :------------: |\n"
        for i in sequence:
            answer = ""
            if start % self.fizz == 0: answer += "Fizz"
            if start % self.buzz == 0: answer += "Buzz"
            if answer == "": answer = start
            if answer != i:
                txt_answer += f"{answer} | {i} | :x:\n"
            else:
                txt_answer += f"{answer} | {i} | :heavy_check_mark:\n"
            start += 1

        now = datetime.now()
        now = now.strftime("%Y%m%d_%H%M")

        text_file = open(f"FizzBuzz_Report_{now}.md", "w")
        text_file.write(txt_answer)
        text_file.close()