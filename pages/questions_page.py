from selenium.webdriver.common.by import By
from .base_page import BasePage


class QuestionsPageLocators:
    QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]


class QuestionsPage(BasePage):
    def click_question(self, index):
        self.click_element(QuestionsPageLocators.QUESTIONS[index])

    def get_answer_text(self, index):
        return self.get_text(QuestionsPageLocators.ANSWERS[index])

    def is_answer_displayed(self, index):
        return self.find_element(QuestionsPageLocators.ANSWERS[index]).is_displayed()