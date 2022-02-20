from django.conf import settings

def user_ip_location(request):
    result = {'ip_address': '', 'region': '', 'country': ''}
    result['ip_address'] = get_client_ip(request)
    if result['ip_address'] == '127.0.0.1' and settings.DEFAULT_IP:
        result['ip_address'] = settings.DEFAULT_IP
    if result['ip_address'] is not None:
        try:
            from django.contrib.gis.geoip2 import GeoIP2
            g = GeoIP2()
            user_data = g.city(result['ip_address'])
            if 'region' in user_data and user_data['region']:
                result['us_state'] = user_data['region']
            if 'country_code' in user_data and user_data['country_code']:
                result['country'] = user_data['country_code']
        except Exception:
            print('Unable to get location information from user IP')
            pass
    return result

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip