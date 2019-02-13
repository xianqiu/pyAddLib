import addlib


if __name__ == '__main__':
    print(addlib.provinces())
    print(addlib.cities('浙江'))
    print(addlib.districts('杭州'))
    print(addlib.get_name('CN007000000'))
    print(addlib.parse_address(city_name='杭州', district_name='西湖'))
    print(addlib.province_codes())
    print(addlib.city_codes('CN007000000'))
    print(addlib.district_codes('CN033001000'))
    print(addlib.get_code(city_name="杭州"))
    print(addlib.get_province_code('浙江'))
    print(addlib.get_city_code('北京'))
    print(addlib.get_district_code(city_name='杭州', district_name='西湖区'))
    print(addlib.parse_code('CN033001012'))
