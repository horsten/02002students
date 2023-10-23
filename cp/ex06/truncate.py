"""Exercise 6.6: Truncate and normalize."""

def truncate_values(float_list : list, settings: dict) -> list: 
    """Return a truncated list of floats given the initial list and the settings for truncating. If normalize is True, the values are first normalized to the [0,1] range and then truncated.
    
    :param float_list: list of floats
    :param settings: Dictionary containing the keys vmin, vmax and normalize with their corresponding values.
    :return: Truncated/Normalized+Truncated values.
    """
    if settings['normalize']:
        maxval = max(abs(min(float_list)), max(float_list))
        float_list = [f / maxval for f in float_list]
    float_list = [min(settings['vmax'], max(settings['vmin'] ,f)) for f in float_list]
    return float_list

    

if __name__ == "__main__":
    # here you can try out your functions
    settings = {'vmin': 0, 'vmax': 2, 'normalize': True}
    float_list = [0.5,0.4,-0.3, 1.5, 2.5, 3.5]
    result=truncate_values(float_list=float_list,settings=settings)
    print(result)
