# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import sys
sys.path.append('/home/xiaoxiao/work/src/TubeTK/Base/Python/pyrpca/examples')
from low_rank_atlas_iter import *

# <codecell>

# global variables
data_folder = ''
reference_im_name = ''
result_folder = ''
selection = []
im_names =[]

# <codecell>

###############################  the main pipeline #############################
def runIteration(Y,lamda):
    low_rank, sparse, n_iter,rank, sparsity = rpca(Y,lamda)
    saveImagesFromDM(low_rank,result_folder+'/LowRank_w'+str(lamda), reference_im_name)
    saveImagesFromDM(sparse,result_folder+'/Sparse_w'+str(lamda), reference_im_name)

    # Visualize and inspect
    fig = plt.figure(figsize=(15,5))
    showSlice(Y, ' Input',plt.cm.gray,0,reference_im_name)
    showSlice(low_rank,' low rank',plt.cm.gray,1, reference_im_name)
    showSlice(sparse,' sparse',plt.cm.gray,2, reference_im_name)
    plt.savefig(result_folder+'/w_'+str(lamda)+'.png')
    fig.clf()
    plt.close(fig)

    num_of_data = Y.shape[1]
    del low_rank, sparse,Y

    return sparsity


def showReferenceImage(reference_im_name):
    im_ref = sitk.ReadImage(reference_im_name) # image in SITK format
    im_ref_array = sitk.GetArrayFromImage(im_ref) # get numpy array
    z_dim, x_dim, y_dim = im_ref_array.shape # get 3D volume shape
    vector_length = z_dim* x_dim*y_dim

    # display reference image
    fig = plt.figure(figsize=(15,5))
    plt.subplot(131)
    implot = plt.imshow(np.flipud(im_ref_array[z_dim/2,:,:]),plt.cm.gray)
    plt.subplot(132)
    implot = plt.imshow(np.flipud(im_ref_array[:,x_dim/2,:]),plt.cm.gray)
    plt.subplot(133)
    implot = plt.imshow(np.flipud(im_ref_array[:,:,y_dim/2]),plt.cm.gray)
    plt.axis('off')
    plt.title('healthy atlas')
    fig.clf()
    del im_ref, im_ref_array
    return

# Affine registering each input image to the reference(healthy atlas)  image
def affineRegistrationStep():
    num_of_data = len(selection)
    for i in range(num_of_data):
        outputIm =  result_folder+'/Iter0_T1_' + str(i)  + '.nrrd'
        AffineReg(reference_im_name,im_names[selection[i]],outputIm)
    return


# <codecell>

# Data info
def useData_BRATS_Challenge():
    global data_folder,result_folder,im_names,selection,reference_im_name
    data_folder = '/home/xiaoxiao/work/data/BRATS/Challenge'

    im_names = [ \
     data_folder+'/HG/0301/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17569.mha',
     data_folder+'/HG/0302/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17573.mha',
     data_folder+'/HG/0303/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17577.mha',
     data_folder+'/HG/0304/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17581.mha',
     data_folder+'/HG/0305/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17585.mha',
     data_folder+'/HG/0306/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17589.mha',
     data_folder+'/HG/0307/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17593.mha',
     data_folder+'/HG/0308/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17597.mha',
     data_folder+'/HG/0309/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17601.mha',
     data_folder+'/HG/0310/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.17605.mha']

    result_folder = '/home/xiaoxiao/work/data/BRATS/Challenge/LRA_Results_T1_Legacy_w1.0'
    os.system('mkdir '+ result_folder)

    # data selection
    selection = [0,1,2,3,4,5,6,7]
    reference_im_name = '/home/xiaoxiao/work/data/SRI24/T1_Crop.nii.gz'
    return (data_folder,result_folder,im_names,selection,reference_im_name)

def useData_BRATS2_Synthetic():
    global data_folder,result_folder,im_names,selection,reference_im_name
    data_folder = '/home/xiaoxiao/work/data/BRATS/BRATS-2/Synthetic_Data/HG'

    im_names = [ \
    data_folder +'/0001/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.866.mha',
    data_folder +'/0002/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.872.mha',
    data_folder +'/0003/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.878.mha',
    data_folder +'/0004/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.884.mha',
    data_folder +'/0005/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.890.mha',
    data_folder +'/0006/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.896.mha',
    data_folder +'/0007/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.902.mha',
    data_folder +'/0008/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.908.mha',
    data_folder +'/0009/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.914.mha',
    data_folder +'/0010/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.920.mha',
    data_folder +'/0011/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.926.mha',
    data_folder +'/0012/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.932.mha',
    data_folder +'/0013/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.938.mha',
    data_folder +'/0014/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.944.mha',
    data_folder +'/0015/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.950.mha',
    data_folder +'/0016/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.956.mha',
    data_folder +'/0017/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.962.mha',
    data_folder +'/0018/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.968.mha',
    data_folder +'/0019/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.974.mha',
    data_folder +'/0020/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.980.mha',
    data_folder +'/0021/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.986.mha',
    data_folder +'/0022/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.992.mha',
    data_folder +'/0023/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.998.mha',
    data_folder +'/0024/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.1004.mha',
    data_folder +'/0025/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.1010.mha'
    ]

    result_folder = '/home/xiaoxiao/work/data/BRATS/BRATS-2/Synthetic_Data/LRA_Results_T1_20inputs_w0.7'

    os.system('mkdir '+ result_folder)
    # data selection
    #selection = [0,1,2,3,4,5,6,7]
    selection = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    reference_im_name = '/home/xiaoxiao/work/data/SRI24/T1_Crop.nii.gz'
    return (data_folder,result_folder,im_names,selection,reference_im_name)


def useData_BRATS2():
    global data_folder,result_folder,im_names,selection,reference_im_name
    data_folder = '/home/xiaoxiao/work/data/BRATS/BRATS-2/Image_Data'

    im_names = [ \
    data_folder+'/HG/0001/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.685.mha',
    data_folder+'/HG/0002/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.692.mha',
    data_folder+'/HG/0003/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.698.mha',
    data_folder+'/HG/0004/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.704.mha',
    data_folder+'/HG/0005/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.710.mha',
    data_folder+'/HG/0006/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.716.mha',
    data_folder+'/HG/0007/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.722.mha',
    data_folder+'/HG/0008/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.728.mha',
    data_folder+'/HG/0009/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.734.mha',
    data_folder+'/HG/0010/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.740.mha',
    data_folder+'/HG/0011/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.746.mha',
    data_folder+'/HG/0012/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.752.mha',
    data_folder+'/HG/0013/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.758.mha',
    data_folder+'/HG/0014/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.764.mha',
    data_folder+'/HG/0015/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.770.mha',
    data_folder+'/HG/0022/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.776.mha',
    data_folder+'/HG/0024/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.782.mha',
    data_folder+'/HG/0025/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.788.mha',
    data_folder+'/HG/0026/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.794.mha',
    data_folder+'/HG/0027/VSD.Brain.XX.O.MR_T1/VSD.Brain.XX.O.MR_T1.800.mha'
    ]
    result_folder = '/home/xiaoxiao/work/data/BRATS/BRATS-2/Image_Data/LRA_Results_20inputs_T1_Test_Weighting'
    os.system('mkdir '+ result_folder)
    # data selection
    selection = range(20)
    reference_im_name = '/home/xiaoxiao/work/data/SRI24/T1_Crop.nii.gz'
    return


# <codecell>

#######################################  main ##################################
#@profile
def main():
    import time
    import resource
    #from guppy import hpy


    ##CropImage(data_folder +'/'+'SRI24/T1.nii.gz',data_folder +'/'+'SRI24/T1_Crop.nii.gz',[50,20,0],[50,30,0])

    #useData_BRATS_Challenge()
    useData_BRATS2()
    #useData_BRATS2_Synthetic()

    s = time.clock()
    # save script to the result folder for paramter checkups
    os.system('cp /home/xiaoxiao/work/src/TubeTK/Base/Python/pyrpca/examples/Test_weighting_Low_Rank_BRATS.py    ' +result_folder)

    #showReferenceImage(reference_im_name)
    affineRegistrationStep()
    im_ref = sitk.ReadImage(reference_im_name) # image in SITK format
    im_ref_array = sitk.GetArrayFromImage(im_ref) # get numpy array
    z_dim, x_dim, y_dim = im_ref_array.shape # get 3D volume shape
    vector_length = z_dim * x_dim * y_dim
    del im_ref, im_ref_array

   # sys.stdout = open(result_folder+'/TestWeighting_RUN.log', "w")
    num_of_data = len(selection)


    NUM_OF_ITERATIONS = 4
    lamda = 0.4
    sparsity = np.zeros(NUM_OF_ITERATIONS)

    Y = np.zeros((vector_length,num_of_data))
    for iterCount in range(1,NUM_OF_ITERATIONS + 1):
        print ' lambda=%f'  %lamda

        # prepare data matrix
        for i in range(num_of_data) :
            im_file =  result_folder+'/'+ 'Iter'+str(0)+'_T1_' + str(i)  + '.nrrd'
            tmp = sitk.ReadImage(im_file)
            tmp = sitk.GetArrayFromImage(tmp)
            Y[:,i] = tmp.reshape(-1)
            del tmp

        sparsity[iterCount-1] = runIteration(Y, lamda)

        gc.collect()
        lamda = lamda + 0.2


    # plot the sparsity curve
    plt.figure()
    plt.plot(range(NUM_OF_ITERATIONS), sparsity)
    plt.savefig(result_folder+'/test_weighting_sparsity.png')




if __name__ == "__main__":
    main()

