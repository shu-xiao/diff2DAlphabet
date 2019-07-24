#!/bin/env python
from ROOT import TFile,TCanvas, TH1F, TH2F, TTree, gROOT, TGaxis, gPad, gStyle 
import sys
def R_pass_fail(x,y,case=0):
    X0Y0 = 0.060723705043
    X0Y1 = -0.0634963039415
    X0Y2 = 0.0300546069188
    X1Y0 = 0.0924660319094
    X1Y1 = -0.0610732451862
    X1Y2 = 0.0377028735669
    X2Y0 = -0.0958794517989
    X2Y1 = 0.102658747646
    X2Y2 = -0.0661771124806
    return X0Y0+X1Y0*x+X2Y0*x**2+X0Y1*y+X1Y1*x*y+X2Y1*x**2*y+X0Y2*y**2+X1Y2*x*y**2+X2Y2*x**2*y**2

def MhTrans(x):
    return (x-100.)/50.

def ZpTrans(x):
    return (x-500.)/2000.

def A0Trans(x):
    return (x-200.)/800.

def main():
    ## print "hello"
    gROOT.SetBatch(1)
    gStyle.SetPaintTextFormat('1.1f')
    output = TFile('diffratio_MA0Mh.root','recreate')
    c1 = TCanvas('c1','c1',1600,1200)
    h_pass = TH2F('h_MhMZp_pass','h_MhMZp_pass',25,100,150,20,500,2500)
    h_pass.Sumw2()
    h_alphabet = TH2F('h_MhMZp_alphabet','h_MhMZp_alphabet',25,100,150,20,500,2500)
    h_alphabet.Sumw2()
    h_dif_alphabet = TH2F('h_dif_alphabet','h_dif_alphabet',25,100,150,20,500,2500)
    h_dif_alphabet.Sumw2()
    h_SB = TH2F('h_MA0hPt_SB','h_MA0hPt_SB',20,200,1000,25,0,500)  ## MA0 vs hPt
    h_SB.Sumw2()
    h_bk = TH2F('h_MA0hPt_bk','h_MA0hPt_bk',20,200,1000,25,0,500)
    h_bk.Sumw2()
    h_dif = TH2F('h_dif','h_dif',20,200,1000,25,0,500)
    h_dif.Sumw2()
    h_SB_MhPt = TH2F('h_SB_MhPt','h_SB_MhPt',25,100,150,25,0,500)
    h_SB_MhPt.Sumw2()
    h_bk_MhPt = TH2F('h_bk_MhPt','h_bk_MhPt',25,100,150,25,0,500)
    h_bk_MhPt.Sumw2()
    h_dif_MhPt = TH2F('h_dif_MhPt','h_dif_MhPt',25,100,150,25,0,500)
    h_dif_MhPt.Sumw2()
    h_SB_MhMA0 = TH2F('h_SB_MhMA0','h_SB_MhMA0',25,100,150,20,200,1000)
    h_SB_MhMA0.Sumw2()
    h_bk_MhMA0 = TH2F('h_bk_MhMA0','h_bk_MhMA0',25,100,150,20,200,1000)
    h_bk_MhMA0.Sumw2()
    h_dif_MhMA0 = TH2F('h_dif_MhMA0','h_dif_MhMA0',25,100,150,20,200,1000)
    h_dif_MhMA0.Sumw2()
    h_SB_Mh = TH1F('h_SB_Mh','h_SB_Mh',25,100,150)
    h_SB_Mh.Sumw2()
    h_bk_Mh = TH1F('h_bk_Mh','h_bk_Mh',25,100,150)
    h_bk_Mh.Sumw2()
    h_SB_MA0 = TH1F('h_SB_MA0','h_SB_MA0',40,200,1000)
    h_SB_MA0.Sumw2()
    h_bk_MA0 = TH1F('h_bk_MA0','h_bk_MA0',40,200,1000)
    h_bk_MA0.Sumw2()
    h_SB_MZp = TH1F('h_SB_MZp','h_SB_MZp',20,500,2500)
    h_SB_MZp.Sumw2()
    h_bk_MZp = TH1F('h_bk_MZp','h_bk_MZp',20,500,2500)
    h_bk_MZp.Sumw2()
    h_SB_hPt = TH1F('h_SB_hPt','h_SB_hPt',50,0,500)
    h_SB_hPt.Sumw2()
    h_bk_hPt = TH1F('h_bk_hPt','h_bk_hPt',50,0,500)
    h_bk_hPt.Sumw2()
    h_dif_MA0 = TH1F('h_dif_MA0','h_dif_MA0',40,200,1000)
    h_dif_MA0.Sumw2()
    h_dif_Mh = TH1F('h_dif_Mh','h_dif_Mh',25,100,150)
    h_dif_Mh.Sumw2()
    h_dif_MZp = TH1F('h_dif_MZp','h_dif_MZp',20,500,2500)
    h_dif_MZp.Sumw2()
    h_dif_hPt = TH1F('h_dif_hPt','h_dif_hPt',50,0,500)
    h_dif_hPt.Sumw2()
    f = TFile('../data/ALLBTagCSV-Run2016_tree.root')
    myTree = f.tree
    # print myTree.GetEntries()
    for en in range(myTree.GetEntries()):
        if (not en% 10000): print en, 'of ', myTree.GetEntries()
        myTree.GetEntry(en)
        # print en, myTree.Mh, myTree.MZp
        #print en, myTree.isTag, myTree.isAntiTag
        if (en>=1000 and len(sys.argv)>=2): break
        ## skip signal
        if (myTree.isTag and myTree.Mh<136 and myTree.Mh>114): continue
        elif (myTree.isTag): 
            h_SB.Fill(myTree.MZp,myTree.hPt)
            h_pass.Fill(myTree.Mh,myTree.MZp)
            h_SB_MhPt.Fill(myTree.Mh,myTree.hPt)
            h_SB_MhMA0.Fill(myTree.Mh,myTree.MA0)
            h_SB_MA0.Fill(myTree.MA0)
            h_SB_hPt.Fill(myTree.hPt)
            h_SB_Mh.Fill(myTree.Mh)
            h_SB_MZp.Fill(myTree.MZp)
        elif (myTree.isAntiTag):
            weight = R_pass_fail(MhTrans(myTree.Mh),A0Trans(myTree.MA0))
            if (weight<0 ): print 'error', en, weight
            h_bk.Fill(myTree.MZp,myTree.hPt,weight)
            h_alphabet.Fill(myTree.Mh,myTree.MZp,weight)
            h_bk_MhPt.Fill(myTree.Mh,myTree.hPt,weight)
            h_bk_MhMA0.Fill(myTree.Mh,myTree.MA0,weight)
            h_bk_MA0.Fill(myTree.MA0,weight)
            h_bk_Mh.Fill(myTree.Mh,weight)
            h_bk_MZp.Fill(myTree.MZp,weight)
            h_bk_hPt.Fill(myTree.hPt,weight)

    h_dif_alphabet.Divide(h_alphabet,h_pass)
    h_dif.Divide(h_bk,h_SB)
    h_dif_MA0.Divide(h_bk_MA0,h_SB_MA0)
    h_dif_Mh.Divide(h_bk_Mh,h_SB_Mh)
    h_dif_MZp.Divide(h_bk_MZp,h_SB_MZp)
    h_dif_hPt.Divide(h_bk_hPt,h_SB_hPt)
    h_dif_MhPt.Divide(h_bk_MhPt,h_SB_MhPt)
    h_dif_MhMA0.Divide(h_bk_MhMA0,h_SB_MhMA0)
    pdfName = 'diff_MA0Mh.pdf'
    c1.Print(pdfName+'[')
    ## gPad.SetLogz()
    h_dif_alphabet.SetMaximum(5.)
    h_dif_alphabet.SetMinimum(0.1)
    h_dif_alphabet.GetZaxis().SetRangeUser(0.1,10)
    h_dif_alphabet.Draw('colz text')
    c1.Print(pdfName)
    h_dif_alphabet.Draw('surf2z')
    c1.Print(pdfName)
    h_dif.Draw('colz text')
    c1.Print(pdfName)
    h_dif.Draw('surf2z')
    c1.Print(pdfName)
    h_dif_MhPt.Draw('colz text')
    c1.Print(pdfName)
    h_dif_MhPt.Draw('surf2z')
    c1.Print(pdfName)
    h_dif_MhMA0.Draw('colz text')
    c1.Print(pdfName)
    h_dif_MhMA0.Draw('surf2z')
    c1.Print(pdfName)
    gPad.SetLogz(0)
    h_dif_Mh.Draw('e')
    c1.Print(pdfName)
    h_dif_MA0.Draw('e')
    c1.Print(pdfName)
    h_dif_MZp.Draw('e')
    c1.Print(pdfName)
    h_dif_hPt.Draw('e')
    c1.Print(pdfName)
    output.Write()

    c1.Print(pdfName+']')
    print "event",h_bk_Mh.Integral(),h_SB_Mh.Integral()
    print "event ratio: ",h_bk_Mh.Integral()/h_SB_Mh.Integral()

if __name__ == '__main__':
    main()
