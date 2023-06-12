'''
 This module make 
    
Athor: Gansior Alexander, gansior@gansior.ru, +79173383804
Starting 2022/25/12
Ending 2022//
    
'''
    
from termcolor import cprint
import inspect
'''
Text colors: grey red green yellow blue magenta cyan white
Text highlights: on_grey on_red on_green on_yellow on_blue on_magenta on_cyan on_white
Attributes: bold dark underline blink reverse concealed
template --> cprint(f'{}' , 'red', attrs=['bold'])
    
    
Shows which module is currently running
cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
'''
    
import os
import sys
from collections import Counter
import copy
import time

ss = time.time() 
    
def prog1(ll, dd, kol):
    kkk = []
    if len(ll)>0:
        for ii in ll:
            kkk.append(ii)
        for _ in range(kol):
            kkk.append(dd)
    else:
        for _ in range(kol):
            kkk.append(dd)
    return kkk

def addSTR(arrayOldSTR:list, kol:int):
    arrayNewSTR = []
    for k in range(kol-1):
        for ssr in arrayOldSTR:
            arrayNewSTR.append(ssr)
    return arrayNewSTR

    
def ZeroStrDict():
    dd={
        'ff_ss': '', 
        'ff_dd': '', 
        'ff_gg':'', 
        'd': '', 
        'kk_uu': '', 
        'kk_rty': '', 
        'vv_cc': '', 
        'vv_cc_df': '', 
        'vv_cc_ht': '', 
        'vv_cc_lo': '', 
        'vv2_cc2_vv3_df3': '',
        'vv2_cc2_vv3_ht3': '',
        'vv2_cc2_vv3_lo3': '',
        'vv2_cc2_df2': '',
        'vv2_cc2_ht2': '',
        'vv2_cc2_lo2': '',
        'vv2_cc2': '', 
        'vv2_cc2_vv3': '',
        'bbb': '',
        'ftcf_ss': '',
        'ftcf_dd': '',
        'ftcf_gg': '',
        'lll': ''
    }
    return dd



def parserDictName(StartName:str, IsDict:dict, statName:Counter):
    for dd in IsDict:
        nn = dd
        if dd.isdigit():
            nn = StartName
        else:
            nn = '_'.join([StartName,dd])
        statName[nn] += 1
        #print(nn, IsDict[dd])
        if type(IsDict[dd]) == dict:
            parserDictName(nn,IsDict[dd],statName)
        if type(IsDict[dd]) == list:
            parserListName(nn,IsDict[dd],statName) 
            
def parserListName(StartName:str, IsDict:list, statName:Counter):
    for dd in IsDict:
        #print(StartName,dd)
        if type(dd) == dict:
            parserDictName(StartName,dd,statName)
        if type(dd) == list:
            parserListName(StartName,dd,statName) 


def parserList(StartName:str, IsDict:list, arrayData:list, LevList:int, StepDict:int, StepList:int):
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
    StartData =  copy.deepcopy(arrayData)
    FirstData =  copy.deepcopy(arrayData) 
    print('LevList === >> ', LevList)
    print('StepList ===== >>>  ',StepList)
    for dd in IsDict:
        #print(StartName,dd)
        
        if type(dd) == dict:
            if LevList ==0:
                StartData = copy.deepcopy(parserDict(StartName, dd, FirstData, LevList, StepDict, StepList))
                arrayData += StartData
                StepList +=1
        elif type(dd) == list:
            LevList += 1
                # if LevList == 0:
                #     arrayData = copy.deepcopy(parserList(StartName,kkdd, arrayData, LevList, StepDict, StepList))
                #     StepList +=1
                #if LevList >= 1:
            StartData = copy.deepcopy(parserList(StartName, dd, FirstData, LevList, StepDict, 0))
            arrayData += StartData
            
    return arrayData


def parserDict(StartName:str, IsDict:dict, arrayData:list, LevList:int, StepDict, StepList):
    cprint('='*20 + ' >> ' + inspect.stack()[0][0].f_code.co_name + ' << '+'='*20, 'red', attrs=['bold'])
    StartData =  copy.deepcopy(arrayData)
    FirstData =  copy.deepcopy(arrayData) 
    print('StepDict ===== >>>  ',StepDict)
    for dd in IsDict:
        nn = dd
        if dd.isdigit():
            nn = StartName
        else:
            nn = '_'.join([StartName,dd])
        if type(IsDict[dd]) == dict:
            if (LevList > 1 and StepList == 1):
                StartData = copy.deepcopy(parserDict(nn,IsDict[dd],FirstData, LevList, StepDict, StepList))
                arrayData += StartData
            if (LevList == 0 and StepList == 1) :
                print('-=-==-=-=-=-=-')
                arrayData = copy.deepcopy(parserDict(nn,IsDict[dd],arrayData, LevList, StepDict, StepList))
                StepDict +=1
                LevList = 1
              
        elif type(IsDict[dd]) == list:
            for kkdd in IsDict[dd]:
                if LevList == 0:
                    arrayData = copy.deepcopy(parserList(nn,IsDict[dd], arrayData, LevList+1, StepDict, StepList))
                    StepList +=1
                if LevList >= 1:
                    StartData = copy.deepcopy(parserList(StartName, dd, FirstData, LevList, StepDict, StepList))
                    arrayData += StartData
                    StepList +=1
            LevList +=1
        else:
            if IsDict[dd]:
                for kk in arrayData:
                    #print("nn ===>> ",nn, "IsDict[dd] == >> ", IsDict[dd])
                    kk[nn] = IsDict[dd]
  
    print('len(arrayData) ==> ', len(arrayData))
    #print("arrayData ===>> ",arrayData)
    return arrayData    
 
if __name__ == '__main__':
       
    d2 = {'d':4, 
        #  'kk': [{'uu':6,'rty':5}], 
        #  'vv': [{'cc':[{'df':44, 'ht':555,'lo':666}, {'df':45, 'ht':565,'lo':676}, {'df':67, 'ht':5658,'lo':6766}]}], 
        #   'bbb':777, 
        #   'ff':[{'ss':'== 888 ===','dd':999, 'gg':1000}, {'ss':'== 333 ===','dd':9599, 'gg':10050}],
        #   'lll':1010,
        'ftcf':[{'ss':888,'dd':999, 'gg':1000}, {'ss':8588,'dd':95777, 'gg':10050}],
          'vv2': [{'cc2':[{'df2':44444, 'ht2':555,'lo2':666}, 
                          {'vv3': [{'df3':449999, 'ht3':55599,'lo3':69696}, 
                                  {'df3':486999, 'ht3':565998,'lo3':676996}
                                 ]}
                        ]
                  }]
          }
    #d2 = isData2
    #ll = prog1(ll, d1, 10)
    #ll = prog1(ll, d2, 5)
    # statName = Counter()   
    result = d2
    # print(result)
    # for kk in result:
    #     if type(kk) == str:
    #         if type(result[kk]) == dict:
    #             parserDictName(kk, result[kk], statName)
    #         elif type(result[kk]) == list:
    #             parserListName(kk, result[kk], statName)
    #         else:
    #             statName[kk] += 1
                
    # print(statName)


    # arrayPlugs = ['statusHistory', 'courierStatusHistory']
    arrayStr =[]
    arrayStr.append(ZeroStrDict())
    for kk in result:
        print(kk, '  ============  ')
        if type(kk) == str:
            if type(result[kk]) == dict:
                arrayStr = copy.deepcopy(parserDict(kk, result[kk], arrayStr, 0, 1,1))
            elif type(result[kk]) == list:
                # if len(result[kk])>1:
                #     arrayStr = addSTR(arrayStr, len(result[kk]))
                arrayStr = copy.deepcopy(parserList(kk, result[kk], arrayStr, 0,1,1))
            else:
                #print(arrayStr)
                for ff in arrayStr:
                    ff[kk] = result[kk]
    print('===========   arrayStr   ================')
    print(arrayStr)
    ff = ZeroStrDict()
    serDict=Counter()
    with open('rezproba.csv', 'w') as r_f:
        strServis = []
        for ll in ff:
            strServis.append(ll)
        r_f.write('^'.join(strServis)+'\n')    
        for sstr in arrayStr:
            strServis = []
            print(sstr)
            print()
            for ll in sstr:
                strServis.append(str(sstr[ll]))
            serDict['^'.join(strServis)] +=1
            r_f.write('^'.join(strServis)+'\n')
            
        # for ldd in serDict:   
        #     r_f.write(ldd)
    print(len(serDict))
        
