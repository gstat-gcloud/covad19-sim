from .settings import *
import urllib.request
import pandas as pd
import json
import os
from typing import IO, Union, Optional
from collections import namedtuple
import datetime
from .getCoronaCases import CovidIsraelUpdate

# dtxl = (datetime.date.today() - datetime.timedelta(days=7)).strftime('%d%m%Y')
# xlpath ="https://govextra.gov.il/media/18101/covid19-data-israel-" + dtxl + ".xlsx"

def main(outdir:Optional[IO]=None)->Union[namedtuple,None]:

    print(__file__, 'is running')
    RECORDS_LIMIT = 10000000

    df = pd.read_csv(GOV_RESOURCE_CSV)

    df['datastore_structure'] = df['resource_id'].apply(lambda resource_id: {'resource_id': resource_id,
                                                                             'limit':RECORDS_LIMIT})        \
                                                 .apply(lambda http_body: str.encode(json.dumps(http_body)))

    df_names = []
    for _, entry in df.iterrows():
        try:
            response = urllib.request.urlopen(entry["url"], entry['datastore_structure'])
            s = json.loads(response.read())
            records = s["result"]["records"]
            data = pd.DataFrame(records).set_index("_id")
            df_names.append([data,entry['name']])
        except:
            print('Failed on:')
            print(entry)
            pass
    # Scraping govpage
    # gov_url = "https://govextra.gov.il/ministry-of-health/corona/corona-virus/"
    # covidIsrael = CovidIsraelUpdate(gov_url)
    # covidIsrael.get_df()
    #
    # df_xls = pd.read_csv(os.path.join(outdir, 'IsraelStatus.csv'))
    # df_out = pd.concat([df_xls, covidIsrael.df])
    # df_out['תאריך'] = pd.to_datetime(df_out['תאריך'])
    # df_out['מספר מאומתים שהתווספו היום'] = ((df_out['מספר מאומתים'] - df_out['מספר מאומתים'].shift(periods=1)) / (
    #             df_out['תאריך'] - df_out['תאריך'].shift(periods=1)).dt.days).fillna(0).astype(int)
    if outdir:
        # df_out.to_csv(os.path.join(outdir, 'IsraelStatus.csv'), index=False)
        for df_name in df_names:
            df = df_name[0]
            filename = df_name[1]+'.csv'
            fullpath = os.path.join(outdir, filename)
            df.to_csv(fullpath)

        retval = None


    else:
        dfs = ([df_name[0] for df_name in df_names])
        names = " ".join([df_name[1] for df_name in df_names])

        Container = namedtuple('dfs', names)
        continer = Container(*dfs)
        retval = continer

    return retval

if __name__ == '__main__':
    main()
