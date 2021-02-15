def there_is_window_other_than(windows):
    """
    :param windows: Массив из окон
    :return: Дескриптор нового окна
    """

    def wrapped(driver):
        new_win = driver.window_handles
        if len(new_win) > len(windows):
            return list(set(new_win).difference(windows))[0]
        else:
            return False

    return wrapped
