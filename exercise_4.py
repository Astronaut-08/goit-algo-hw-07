'''Реалізуйте структуру даних для системи коментарів так, щоб коментарі могли мати відповіді, які,
в свою чергу, також могли мати відповіді, формуючи таким чином ієрархічну структуру.

Також візьміть до уваги наступні вимоги:

Реалізуйте клас Comment, що представляє собою окремий коментар.
Він має зберігати текст коментаря, автора та список відповідей.
Метод класу add_reply має додавати нову відповідь до коментаря.
Метод класу remove_reply має видаляти відповідь із коментаря.
Це має змінювати текст коментаря на стандартне повідомлення (наприклад, "Цей коментар було видалено.")
і встановлювати прапорець is_deleted в True.
Метод display має рекурсивно виводити коментар та всі його відповіді,
використовуючи відступи для відображення ієрархічної структури.'''

from typing import Callable

class Comment:
    def __init__(self, comment: str, name: str):
        self.comment = comment
        self.name = name
        self.threads = []
        # Status
        self.is_delete = False

    def add_reply(self, reply: Callable):
        '''Додає коментар до повідомлення'''
        self.threads.append(reply)

    def remove_reply(self):
        '''Видаляє коментар до повідомлення'''
        self.is_delete = True
        self.comment = 'Цей коментар було видалено.'

    def display(self, left_tab=''):
        '''Рекурсивно відображає коментар та всі його треди'''
        if self.is_delete:
            print(f'{left_tab}{self.comment}')
        else:
            print(f'{left_tab}{self.name}: {self.comment}')

        if self.threads:
            left_tab += '   '
            for thread in self.threads:
                thread.display(left_tab) # рекурсивний виклик тут


#################################################### Приклад очікуваного результату
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
