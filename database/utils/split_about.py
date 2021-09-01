def split_about(about):
    about_short_symbols = 200

    if len(about) <= about_short_symbols:
        return [about, '']
    else:
        last_period_index = about_short_symbols - about[0:about_short_symbols][::-1].index('.')
        return [about[0:last_period_index],
                about[last_period_index + 1:len(about)]]
