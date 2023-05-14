params = {
    'company_hiring': (
        '[К,к]омпан[и,i][я,и,й][^\,"\n]{1,3}[#А-ЯA-Z][a-zA-Zа-яА-Я0-9]{2,20}[^\,"\n]{1}«{0,1}[А-ЯA-Z]{0,20}[A-ZА-Яa-zа-я]{0,20}',
        '[C,c]ompany[^\,"\n]{1,3}[#А-ЯA-Z][a-zA-Zа-яА-Я0-9]{2,20}[^\,"\n]{1}«{0,1}[А-ЯA-Z]{0,20}[A-ZА-Яa-zа-я]{0,20}',
        '[Р,р]аботодатель[^\,"\n]{1,3}[#А-ЯA-Z][a-zA-Zа-яА-Я0-9]{2,20}[^\,"\n]{1}«{0,1}[А-ЯA-Z]{0,20}[A-ZА-Яa-zа-я]{0,20}'),
    'country': (),
    'remote': ('[Rr]emote', '[Уу]дал[ёе][н]{1,2}[кыйоая]{0,2}', '[вВ]iддален[ийка]{0,2}', '[Гг]ибридн[ыйоеая]{0,2}',
               '[Оо]фис[\W]{1,3}[Гг\.]{0,3}[\W]{0,1}[A-ZА-Я]{1}[a-zа-я]{2,}'),
    'jobs_type': ('[Ff]ull[\W]{0,1}[Tt]ime', '[Зз]анятость[\W]{0,3}[Пп]олная', '[Пп]олная[\W]{1,3}[Зз]анятость',
                  'из офиса'),
    'english_level': (
        '[Ee]nglish[\W]{0,2}[A-Za-zА-Яа-я][\W]{0,3}[\d]', '[Uu]pper[\W]{0,1}intermediate', '[Ii]ntermediate',
        '[Pp]re[\W]{0,1}[Ii]ntermediate', '[Uu]pper'),

    'country_list': ('Panama', 'Philippines', 'Europe', 'World', 'United Arab Emirates', 'Argentina', 'Armenia',
                     'Australia', 'Austria', 'Azerbaijan', 'Belgium', 'Bulgaria', 'Belarus', 'Brazil',
                     'Central African Republic', 'Canada', 'Switzerland', 'Chile', 'China', 'Colombia',
                     'Costa Rica', 'Cuba', 'Cyprus', 'Czechia', 'Germany', 'Denmark', 'Dominican Republic',
                     'Ecuador', 'Egypt', 'Spain', 'Estonia', 'Finland', 'France', 'Great Britain',
                     'Georgia', 'Greece', 'Croatia', 'Hungary', 'Indonesia', 'India', 'Ireland',
                     'Iceland', 'Israel', 'Italy', 'Japan', 'Kazakhstan', 'Kyrgyzstan', 'South Korea',
                     'Lithuania', 'Luxembourg', 'Latvia', 'Monaco', 'Moldova', 'Mexico', 'Montenegro',
                     'Mongolia', 'Malaysia', 'Netherlands', 'Norway', 'New Zealand', 'Oman', 'Poland',
                     'Portugal', 'Qatar', 'Romania', 'Russian Federation', 'Singapore', 'Serbia',
                     'Slovakia', 'Slovenia', 'Sweden', 'Thailand', 'Tajikistan', 'Tunisia', 'Turkey',
                     'Ukraine', 'Uruguay', 'USA', 'Uzbekistan', 'Vietnam'),

    'relocation': ('[Рр]елокация', 'relocation', 'relocate'),
    'country_relocation': (),
    'possibility_relocaton': (),
    'experience': {"[0-9] лет|[0-9] год|[0-9] year", },
    'english_for_shorts': {'[Bb][^\na-zA-Zа-яА-Я0-9]?1|[Bb][^\na-zA-Zа-яА-Я0-9]?0|[Bb][^\na-zA-Zа-яА-Я0-9]?2|'
                           '[Aa][^\na-zA-Zа-яА-Я0-9]?1|[Aa][^\na-zA-Zа-яА-Я0-9]?0|[Aa][^\na-zA-Zа-яА-Я0-9]?2|'
                           '[Pp]re[^\na-zA-Zа-яА-Я][Ii]ntermediate|[Ii]ntermediate|[Uu]pper|[Aa]dvance|[Рр]азговорный', },
    'salary_for_shorts': {'[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*₽|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*\$|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*€|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*руб|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*млн|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*KZT|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*USD|'
                          '[0-9]{1,3}[^\n%A-Za-zА-Яа-я]{0,1}[0-9]{1,3}[^\n]*EUR', },

}
