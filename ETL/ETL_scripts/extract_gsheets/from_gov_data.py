import pandas as pd


path_in = "C:\\Users\\User\\PycharmProjects\\covad19-sim\\ETL\\DW\\raw_data\\gov_yishuv\\"
path_out = "C:\\Users\\User\\PycharmProjects\\covad19-sim\\Resources\\Datasets\\IsraelData\\"


def make_file(file, dt):
    t = pd.read_excel(path_in + file, skiprows=4, sheet_name="כלל הארץ לפרסום")
    t = t.drop(columns=['Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14'])
    colnames = t.columns
    new_names = \
        [
            "יישוב",
            "pop2018",
            "מספר נבדקים",
            "מספר חולים מאומתים",
            "מספר מחלימים",
            "pct_growth_3",
            "last3days",
            "per_100k",
            "junk",
        ]
    t.columns = new_names
    t = t.melt(id_vars=new_names[0:2], value_vars=new_names[2:])
    t = t[~t['variable'].isin(['pct_growth_3', 'junk', 'per_100k'])]
    t['value'] = pd.to_numeric(t['value'], errors='coerce').fillna(0).astype(int)
    t = t.rename(columns={'variable': 'סוג מידע'})
    t['date'] = pd.to_datetime(dt)
    t.loc[:, 'StringencyIndex'] = None
    t.to_csv(path_out + 'yishuv_' + dt + ".csv", index=False)
    return t


files = ["כלל הארץ לשליחה 26.04.20 שעה 09.00.xlsx",
         "כלל הארץ 24.04.20 לשליחה.xlsx",
         "20.04 כלל הארץ לשליחה.xlsx",
         "כלל הארץ לפרסום 30.04.20 שעה 08.00.xlsx",
         "כלל הארץ לשליחה 29.04.20 שעה 08.00.xlsx",
         "כלל_הארץ_ומועצות_אזוריות_01_05_לפרסום.xlsx",
         "כלל_הארץ_ומועצות_אזוריות_02_05_שעה_08_00_לפרסום.xlsx",
         "דוח_חדש_כלל_הארץ_כולל_מועצות_אזוריות_04_05_20_שעה_20_30.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_06_05_20_שעה_11_00.xlsx",
         "כלל_הארץ_כולל_מועצות_אזוריות_לפרסום_05_05_שעה_11_00.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_08_05_20_שעה_11_00.xlsx",
         "1589011501844_דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_09_05_20_שעה.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_10_05_20_שעה_11_00.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_11_05_20_שעה_11_00.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_12_05_20_שעה_11_00.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_15_05_20_שעה_11_00.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_18_05_20_שעה_11_00.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_20_05_20_שעה_19_30.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_21_05_20_שעה_19_30.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_24_05_20_שעה_19_30.xlsx",
         "דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_25_05_20_שעה_19_30.xlsx",
         'דוח_אקסל_כלל_הארץ_כולל_מועצות_אזוריות_29_05_20_שעה_19_30.xlsx',
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_31_05_20_שעה_19_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_02_06_20_שעה_19_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_04_06_20_שעה_19_00.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_07_06_20_שעה_19_00.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_08_06_20_שעה_19_30.xlsx",
         "1591719654425_דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_09_06_20.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_11_06_20_שעה_19_20.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_13_06_20_שעה_19_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_15_06_20_שעה_19_20.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_16_06_20_שעה_19_10.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_17_6_20_שעה_19_40 (1).xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_22_06_20_שעה_10_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_23_06_20_שעה_19_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_24_06_20_שעה_10_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_25_06_20_שעה_10_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_26_06_20_שעה_18_00.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_27_06_20_שעה_21_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_28_06_20_שעה_10_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_29_06_20_שעה_11_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_30_06_20_שעה_19_00.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_01_07_20_שעה_10_30.xlsx",
         "1593676447268_דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_02_07_20.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_03_07_20_שעה_08_00.xlsx",
         "1593885765338_דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_04_07_20.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_05_07_20_שעה_10_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_06_07_20_שעה_10_00.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_07_07_20_שעה_08_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_08_07_20_שעה_10_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_09_07_20_שעה_10_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_14_07_20_שעה_13_00 (1).xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_23_07_20_שעה_10_30.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_02_08_20_שעה_11_00.xlsx",
         "דוח_אקסל_חדש_כלל_הארץ_כולל_מועצות_אזוריות_06_08_20_שעה_10_30.xlsx"
         ]

dates = ['20200508',
         '20200509',
         '20200510',
         '20200511',
         '20200512',
         '20200515',
         '20200518',
         '20200519',
         '20200521',
         '20200524',
         '20200525',
         '20200529',
         '20200531',
         '20200602',
         '20200604',
         '20200607',
         '20200608',
         '20200609',
         '20200611',
         '20200613',
         '20200615',
         '20200616',
         '20200617',
         '20200622',
         '20200623',
         '20200624',
         '20200625',
         '20200626',
         '20200627',
         '20200628',
         '20200629',
         '20200630',
         '20200701',
         '20200702',
         '20200703',
         '20200704',
         '20200705',
         '20200706',
         '20200707',
         '20200708',
         '20200709',
         '20200714',
         '20200723',
         '20200802',
         '20200806',
         ]
file = files[-1]
dt = dates[-1]
make_file(file, dt)

# -----------------------------Join files------------------------

p24 = pd.read_csv(path_out + 'yishuv_' + '20200723' + ".csv")
p24['date'] = pd.to_datetime('20200724')
p25 = p24.copy()
p25['date'] = pd.to_datetime('20200725')
p26 = p24.copy()
p26['date'] = pd.to_datetime('20200726')
p27 = p24.copy()
p27['date'] = pd.to_datetime('20200727')
p28 = p24.copy()
p28['date'] = pd.to_datetime('20200728')
p29 = p24.copy()
p29['date'] = pd.to_datetime('20200729')
p30 = p24.copy()
p30['date'] = pd.to_datetime('20200730')
p31 = p24.copy()
p31['date'] = pd.to_datetime('20200731')
p01 = p24.copy()
p01['date'] = pd.to_datetime('20200801')
p02 = pd.read_csv(path_out + 'yishuv_' + '20200802' + ".csv")
p03 = p02.copy()
p03['date'] = pd.to_datetime('20200803')
p04 = p02.copy()
p04['date'] = pd.to_datetime('20200804')
p05 = p02.copy()
p05['date'] = pd.to_datetime('20200805')
p06 = pd.read_csv(path_out + 'yishuv_' + '20200806' + ".csv")





joined = pd.concat([p24, p25, p26, p27, p28, p29, p30, p31, p01, p02, p03, p04, p05, p06])
joined = joined.dropna(subset=['יישוב', 'pop2018'])

yishuv_file = pd.read_csv(path_out + 'yishuv_file.csv')
yishuv_file = pd.concat([yishuv_file, joined])
yishuv_file['last_updated'] = pd.to_datetime('20200806')
yishuv_file['date'] = pd.to_datetime(yishuv_file['date']).dt.date
yishuv_file.to_csv(path_out + 'yishuv_file.csv', index=False)

# temp = pd.read_csv("C:\\Users\\User\\PycharmProjects\\covad19-sim\\Resources\\Datasets\\IsraelData\\gsheets.csv")
