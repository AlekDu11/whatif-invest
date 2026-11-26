# /bonuses/ — sign-up and invite-a-friend bonuses by country (owner 2026-11-25). Data: data/bonuses.json. Languages: uk, ru, en (more with more countries).
BON_LANGS = ('uk', 'ru', 'en')
BON = {
 'uk': dict(nav='Бонуси за реєстрацію', title='Бонуси за реєстрацію {y}: {n} перевірених пропозицій з умовами', d='Гроші й подарунки за реєстрацію та запрошення друзів: банки, інвестиції, крипта. Чесно: скільки дають, що треба зробити, чи можна вивести. Оновлено {d}.',
            h1='Бонуси за реєстрацію: {n} перевірених пропозицій', lead='Банки й інвестиційні сервіси платять за реєстрацію та за кожного друга, якого ти запросиш. Ми зібрали ті, що діють зараз, з чесними умовами: скільки дають, що треба зробити і чи можна ці гроші вивести. Списки згруповані за країнами.',
            you='Ти отримуєш', friend='За запрошення', need='Що треба зробити', cash='Чи можна вивести', until='Діє до', nolimit='без строку', checked='Умови перевірено', src='Джерело', go='Отримати бонус', more='Детально', allc='Усі країни',
            how_h='Як заробляти, запрошуючи друзів', how=['Зареєструйся за посиланням і отримай свій бонус.', 'У застосунку знайди своє особисте посилання (зазвичай у профілі або в розділі «Запроси друга»).', 'Надішли його сім’ї та друзям, поясни, що це, і чесно скажи про умови. За кожного, хто зареєструється, бонус отримаєте обоє.'],
            warn_h='Чесно про бонуси', warn=['Бонус — приємний додаток, а не заробіток, з якого можна жити.', 'Не відкривай кредитні ліміти і не бери позик заради бонусу.', 'Умови змінюються: перед реєстрацією перевір їх у застосунку чи на сайті сервісу.', 'Посилання на цій сторінці — партнерські: ми теж отримуємо бонус, для тебе умови від цього не змінюються.'],
            suggest='Знаєш чесний бонус, якого тут немає? Напиши нам у Telegram — додамо після перевірки.', upd='Оновлено'),
 'ru': dict(nav='Бонусы за регистрацию', title='Бонусы за регистрацию {y}: {n} проверенных предложений с условиями', d='Деньги и подарки за регистрацию и приглашение друзей: банки, инвестиции, крипта. Честно: сколько дают, что нужно сделать, можно ли вывести. Обновлено {d}.',
            h1='Бонусы за регистрацию: {n} проверенных предложений', lead='Банки и инвестиционные сервисы платят за регистрацию и за каждого друга, которого ты пригласишь. Мы собрали те, что действуют сейчас, с честными условиями: сколько дают, что нужно сделать и можно ли эти деньги вывести. Списки сгруппированы по странам.',
            you='Ты получаешь', friend='За приглашение', need='Что нужно сделать', cash='Можно ли вывести', until='Действует до', nolimit='без срока', checked='Условия проверены', src='Источник', go='Получить бонус', more='Подробно', allc='Все страны',
            how_h='Как зарабатывать, приглашая друзей', how=['Зарегистрируйся по ссылке и получи свой бонус.', 'В приложении найди свою личную ссылку (обычно в профиле или в разделе «Пригласи друга»).', 'Отправь её семье и друзьям, объясни, что это, и честно расскажи об условиях. За каждого, кто зарегистрируется, бонус получите оба.'],
            warn_h='Честно о бонусах', warn=['Бонус — приятное дополнение, а не заработок, на который можно жить.', 'Не открывай кредитные лимиты и не бери займы ради бонуса.', 'Условия меняются: перед регистрацией проверь их в приложении или на сайте сервиса.', 'Ссылки на этой странице — партнёрские: мы тоже получаем бонус, для тебя условия от этого не меняются.'],
            suggest='Знаешь честный бонус, которого здесь нет? Напиши нам в Telegram — добавим после проверки.', upd='Обновлено'),
 'en': dict(nav='Sign-up bonuses', title='Sign-up bonuses {y}: {n} checked offers with their terms', d='Money and gifts for signing up and inviting friends: banks, investing, crypto. Honest terms: how much, what to do, whether you can withdraw it. Updated {d}.',
            h1='Sign-up bonuses: {n} checked offers', lead='Banks and investing apps pay you for signing up and for every friend you invite. We list the ones running now, with honest terms: how much you get, what you have to do and whether you can withdraw it. Grouped by country.',
            you='You get', friend='For inviting', need='What to do', cash='Can you withdraw it?', until='Valid until', nolimit='no end date', checked='Terms checked', src='Source', go='Get the bonus', more='Details', allc='All countries',
            how_h='How to earn by inviting friends', how=['Sign up through the link and collect your bonus.', 'Find your personal invite link in the app (usually in your profile or an «Invite a friend» section).', 'Send it to family and friends, explain what it is and be honest about the terms. For everyone who signs up, you both get the bonus.'],
            warn_h='The honest part', warn=['A bonus is a nice extra, not an income to live on.', "Don't open credit limits or take loans for a bonus.", 'Terms change: check them in the app or on the provider’s site before you sign up.', 'Links on this page are partner links: we get a bonus too, and your terms stay the same.'],
            suggest='Know an honest bonus that is missing here? Message us on Telegram — we add it after checking.', upd='Updated'),
}

# header 🎁 button, «Exclusive offers» popup and the partner strip (owner 2026-11-26)
BONX = {
 'uk': dict(btn='Бонуси', title='Ексклюзивні пропозиції', sub='Перевірені бонуси для новачків', steps=['Реєстрація', 'Депозит', 'Отримай бонус'], open='Відкрити', upto='до', partner='Партнер',
            all='Усі бонуси з умовами', ex='Біржі: бонуси новачкам', rec='Рекомендуємо', local='Для твоєї країни',
            note='Бонуси виплачує біржа чи сервіс після реєстрації й виконання умов. «До» — максимум за правилами біржі; новачку зазвичай дістаються купони на десятки доларів за перші кроки.',
            strip='Новачок на {n}? {l}'),
 'ru': dict(btn='Бонусы', title='Эксклюзивные предложения', sub='Проверенные бонусы для новичков', steps=['Регистрация', 'Депозит', 'Получи бонус'], open='Открыть', upto='до', partner='Партнёр',
            all='Все бонусы с условиями', ex='Биржи: бонусы новичкам', rec='Рекомендуем', local='Для твоей страны',
            note='Бонусы выплачивает биржа или сервис после регистрации и выполнения условий. «До» — максимум по правилам биржи; новичку обычно достаются купоны на десятки долларов за первые шаги.',
            strip='Новичок на {n}? {l}'),
 'en': dict(btn='Bonuses', title='Exclusive offers', sub='Checked bonuses for new users', steps=['Sign up', 'Deposit', 'Get the bonus'], open='Open', upto='up to', partner='Partner',
            all='All bonuses with terms', ex='Exchanges: new user bonuses', rec='Recommended', local='For your country',
            note='The exchange or service pays the bonus after sign-up and meeting its terms. «Up to» is the maximum under the exchange’s rules; new users usually get vouchers worth tens of dollars for the first steps.',
            strip='New to {n}? {l}'),
}
