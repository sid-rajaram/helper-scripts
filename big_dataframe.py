import cPickle, gzip
from numpy import savetxt, loadtxt
from pandas import DataFrame

def bigsave(df,fname):
    if fname[-3:]=='.gz':
        fname = fname[-3:]
    savetxt(fname+'.values.gz',df.values)
    cPickle.dump(df.index,gzip.open(fname+'.index.gz','wb'))
    cPickle.dump(df.columns,gzip.open(fname+'.columns.gz','wb'))
    cPickle.dump(df.dtypes,gzip.open(fname+'.dtypes.gz','wb'))

def bigload(fname):
    if fname[-3:]=='.gz':
        fname = fname[-3:]
    df = DataFrame(data=loadtxt(fname+'.values.gz'),
                   index=cPickle.load(gzip.open(fname+'.index.gz','rb')),
                   columns=cPickle.load(gzip.open(fname+'.columns.gz','rb')),
                   dtype=cPickle.load(gzip.open(fname+'.dtypes.gz','rb')))
    return df
