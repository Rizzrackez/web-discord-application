from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

BOT_COMMANDS = (
    ('Тестовое сообщение', 'Тестовое сообщение'),
    ('Конвертация видео с ютуб в m4a файл', 'Конвертация видео с ютуб в m4a файл'),
    ('Случайный фильм', 'Случайный фильм'),
    ('Конвертер валют', 'Конвертер валют')
)

CURRENCY = (('AED', 'AED'), ('AFN', 'AFN'), ('ALL', 'ALL'), ('AMD', 'AMD'), ('ANG', 'ANG'), ('AOA', 'AOA'),
            ('ARS', 'ARS'), ('AUD', 'AUD'), ('AWG', 'AWG'), ('AZN', 'AZN'), ('BAM', 'BAM'), ('BBD', 'BBD'),
            ('BDT', 'BDT'), ('BGN', 'BGN'), ('BHD', 'BHD'), ('BIF', 'BIF'), ('BMD', 'BMD'), ('BND', 'BND'),
            ('BOB', 'BOB'), ('BRL', 'BRL'), ('BSD', 'BSD'), ('BTC', 'BTC'), ('BTN', 'BTN'), ('BWP', 'BWP'),
            ('BYN', 'BYN'), ('BZD', 'BZD'), ('CAD', 'CAD'), ('CDF', 'CDF'), ('CHF', 'CHF'), ('CLP', 'CLP'),
            ('CNY', 'CNY'), ('COP', 'COP'), ('CRC', 'CRC'), ('CUP', 'CUP'), ('CVE', 'CVE'), ('CZK', 'CZK'),
            ('DJF', 'DJF'), ('DKK', 'DKK'), ('DOP', 'DOP'), ('DZD', 'DZD'), ('EGP', 'EGP'), ('ERN', 'ERN'),
            ('ETB', 'ETB'), ('EUR', 'EUR'), ('FJD', 'FJD'), ('FKP', 'FKP'), ('GBP', 'GBP'), ('GEL', 'GEL'),
            ('GHS', 'GHS'), ('GIP', 'GIP'), ('GMD', 'GMD'), ('GNF', 'GNF'), ('GTQ', 'GTQ'), ('GYD', 'GYD'),
            ('HKD', 'HKD'), ('HNL', 'HNL'), ('HRK', 'HRK'), ('HTG', 'HTG'), ('HUF', 'HUF'), ('IDR', 'IDR'),
            ('ILS', 'ILS'), ('INR', 'INR'), ('IQD', 'IQD'), ('IRR', 'IRR'), ('ISK', 'ISK'), ('JMD', 'JMD'),
            ('JOD', 'JOD'), ('JPY', 'JPY'), ('KES', 'KES'), ('KGS', 'KGS'), ('KHR', 'KHR'), ('KMF', 'KMF'),
            ('KPW', 'KPW'), ('KRW', 'KRW'), ('KWD', 'KWD'), ('KYD', 'KYD'), ('KZT', 'KZT'), ('LAK', 'LAK'),
            ('LBP', 'LBP'), ('LKR', 'LKR'), ('LRD', 'LRD'), ('LSL', 'LSL'), ('LYD', 'LYD'), ('MAD', 'MAD'),
            ('MDL', 'MDL'), ('MGA', 'MGA'), ('MKD', 'MKD'), ('MMK', 'MMK'), ('MNT', 'MNT'), ('MOP', 'MOP'),
            ('MRO', 'MRO'), ('MUR', 'MUR'), ('MVR', 'MVR'), ('MWK', 'MWK'), ('MXN', 'MXN'), ('MYR', 'MYR'),
            ('MZN', 'MZN'), ('NAD', 'NAD'), ('NGN', 'NGN'), ('NIO', 'NIO'), ('NOK', 'NOK'), ('NPR', 'NPR'),
            ('NZD', 'NZD'), ('OMR', 'OMR'), ('PAB', 'PAB'), ('PEN', 'PEN'), ('PGK', 'PGK'), ('PHP', 'PHP'),
            ('PKR', 'PKR'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('QAR', 'QAR'), ('RON', 'RON'), ('RSD', 'RSD'),
            ('RUB', 'RUB'), ('RWF', 'RWF'), ('SAR', 'SAR'), ('SBD', 'SBD'), ('SCR', 'SCR'), ('SDG', 'SDG'),
            ('SEK', 'SEK'), ('SGD', 'SGD'), ('SHP', 'SHP'), ('SLL', 'SLL'), ('SOS', 'SOS'), ('SRD', 'SRD'),
            ('STD', 'STD'), ('SVC', 'SVC'), ('SYP', 'SYP'), ('SZL', 'SZL'), ('THB', 'THB'), ('TJS', 'TJS'),
            ('TMT', 'TMT'), ('TND', 'TND'), ('TOP', 'TOP'), ('TRY', 'TRY'), ('TTD', 'TTD'), ('TWD', 'TWD'),
            ('TZS', 'TZS'), ('UAH', 'UAH'), ('UGX', 'UGX'), ('USD', 'USD'), ('UYU', 'UYU'), ('UZS', 'UZS'),
            ('VEF', 'VEF'), ('VND', 'VND'), ('VUV', 'VUV'), ('WST', 'WST'), ('XAF', 'XAF'), ('XCD', 'XCD'),
            ('XDR', 'XDR'), ('XOF', 'XOF'), ('XPF', 'XPF'), ('YER', 'YER'), ('ZAR', 'ZAR'), ('ZMW', 'ZMW'),
            ('ZWB', 'ZWB'))


class BotInteraction(models.Model):
    discord_tag = models.CharField(max_length=20)
    youtube = models.CharField(max_length=120, blank=True, null=True)
    command = models.CharField(max_length=100, choices=BOT_COMMANDS, default=1)
    currency_from = models.CharField(max_length=3, choices=CURRENCY, default='USD')
    currency_to = models.CharField(max_length=3, choices=CURRENCY, default='RUB')

    class Meta:
        verbose_name = "Bot Interaction"
        verbose_name_plural = "Bot Interactions"

    def __str__(self):
        return self.discord_tag


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    discord_tag = models.CharField(max_length=20, unique=True, blank=True, null=True)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserProfile.objects.create(user=instance)
