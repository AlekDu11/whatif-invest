# -*- coding: utf-8 -*-
"""Per-stock metric pages /<id>/market-cap/, /<id>/revenue/, /<id>/earnings/ (en + uk; other languages later).
Placeholders: {name} {tk} {m} month-year {v} value {r} world rank {y} fiscal year {g} growth."""
SM = {
 'en': dict(
    nav={'market-cap': 'Market cap', 'revenue': 'Revenue', 'earnings': 'Earnings'},
    mc_t='{name} ({tk}) market cap: {v} — history and rank', mc_h1='{name} market cap',
    mc_d='{name} ({tk}) is worth {v} as of {m}, #{r} among the world’s largest public companies. Market cap history by year, chart and peers.',
    mc_a='As of {m}, {name} ({tk}) has a market capitalization of {v}, which makes it #{r} among the world’s largest public companies.',
    mc_a1='Over the past year its value changed by {g}.',
    rv_t='{name} ({tk}) revenue {y}: {v} ({g}) — annual history', rv_h1='{name} revenue',
    rv_d='{name} ({tk}) revenue was {v} in fiscal {y} ({g} year over year). Annual revenue history, growth and trailing 12 months.',
    rv_a='{name} ({tk}) reported revenue of {v} for fiscal year {y}, {g} compared with the year before.',
    rv_ttm='Over the last 12 months revenue was {v}.',
    ea_t='{name} ({tk}) earnings {y}: net income {v} — annual history', ea_h1='{name} earnings (net income)',
    ea_d='{name} ({tk}) earned {v} of net income in fiscal {y} ({g} year over year). Annual profit history, margins and trailing 12 months.',
    ea_a='{name} ({tk}) earned a net income of {v} in fiscal year {y}, {g} compared with the year before.',
    ea_m='Net profit margin: {v} of revenue.',
    year='Year', val='Value', chg='Change', margin='Margin', price='Share price', rank='World rank', y1='1 year',
    est='Market cap history is an estimate: monthly closing price × today’s share count, in US dollars at today’s exchange rate.',
    fx='Converted to US dollars at today’s exchange rate.', src='Data: company filings via Yahoo Finance, updated {d}. Not investment advice.',
    chart_mc='Market cap over time', chart_rv='Revenue by year', chart_ea='Net income by year', table='By year',
    more='More about {name}', peers='Largest companies in the world', loss='loss'),
 'uk': dict(
    nav={'market-cap': 'Капіталізація', 'revenue': 'Виручка', 'earnings': 'Прибуток'},
    mc_t='Капіталізація {name} ({tk}): {v} — історія і місце у світі', mc_h1='Ринкова капіталізація {name}',
    mc_d='{name} ({tk}) коштує {v} станом на {m} — №{r} серед найбільших публічних компаній світу. Історія капіталізації по роках і графік.',
    mc_a='Станом на {m} ринкова капіталізація {name} ({tk}) — {v}, це №{r} серед найбільших публічних компаній світу.',
    mc_a1='За останній рік вартість компанії змінилася на {g}.',
    rv_t='Виручка {name} ({tk}) за {y}: {v} ({g}) — історія по роках', rv_h1='Виручка {name}',
    rv_d='Виручка {name} ({tk}) за {y} фінансовий рік — {v} ({g} до попереднього року). Історія виручки, зростання і останні 12 місяців.',
    rv_a='{name} ({tk}) отримала {v} виручки за {y} фінансовий рік — {g} порівняно з роком раніше.',
    rv_ttm='За останні 12 місяців виручка становила {v}.',
    ea_t='Прибуток {name} ({tk}) за {y}: {v} — історія по роках', ea_h1='Чистий прибуток {name}',
    ea_d='Чистий прибуток {name} ({tk}) за {y} фінансовий рік — {v} ({g} до попереднього року). Історія прибутку, маржа і останні 12 місяців.',
    ea_a='{name} ({tk}) заробила {v} чистого прибутку за {y} фінансовий рік — {g} порівняно з роком раніше.',
    ea_m='Чиста маржа: {v} від виручки.',
    year='Рік', val='Значення', chg='Зміна', margin='Маржа', price='Ціна акції', rank='Місце у світі', y1='За рік',
    est='Історія капіталізації — оцінка: місячна ціна закриття × поточна кількість акцій, у доларах США за сьогоднішнім курсом.',
    fx='Переведено в долари США за сьогоднішнім курсом.', src='Дані: звітність компанії через Yahoo Finance, оновлено {d}. Не є інвестиційною порадою.',
    chart_mc='Капіталізація в часі', chart_rv='Виручка по роках', chart_ea='Чистий прибуток по роках', table='По роках',
    more='Усе про {name}', peers='Найбільші компанії світу', loss='збиток'),
}
SM_LANGS = tuple(SM)
SM_KINDS = ('market-cap', 'revenue', 'earnings')
