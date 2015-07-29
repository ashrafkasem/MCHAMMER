#!/usr/bin/python
import os,sys
from math import sqrt
from ROOT import TCanvas,ROOT,TFile,TLegend,TF1,TLine,gROOT,TPaveText,TH1D,Double,TH2D,THStack,gStyle
from plotting.PlotStyle import setPlotStyle,calcSigma,drawLabelCmsPrivateSimulation,colorRwthDarkBlue
from plotting.PlotStyle import colorRwthMagenta,setupAxes,convertToHcalCoords,chimney1,chimney2,printProgress
from plotting.PlotStyle import setStatBoxOptions, setStatBoxPosition
from plotting.RootFileHandler import RootFileHandler
from matchingLibrary import findBestL1Match
from array import array

setPlotStyle()

gROOT.ProcessLine(".L $HOMUONTRIGGER_BASE/python/loader.C+");

prefix = '[makeEvsEtaPhiPlot] '
def output(outString):
	print prefix,outString

if len(sys.argv) < 2:
	print 'First argument has to be the file name scheme!'
fileHandler = RootFileHandler(sys.argv[1])
fileHandler.printStatus()

if( not os.path.exists('plots')):
	os.mkdir('plots')
if( not os.path.exists('plots/controlPlots')):
	os.mkdir('plots/controlPlots')

'''
Control Plot that shows the number of matches in Det Ids for a given RecHit Det id
'''
def plotHoDigiMatchesPerDetId():
	canvas = TCanvas('canvasDigiMatchesMultiplicity')
	digiMatches = fileHandler.getHistogram('hoMuonAnalyzer/hoDigiMatchesPerDetId_Multiplicity')
	setupAxes(digiMatches)
	digiMatches.SetTitle('Number of matches between RecHit and Digi for a given DetId')
	digiMatches.GetXaxis().SetRangeUser(0,5)
	digiMatches.GetXaxis().SetTitle('Number of matches per DetId')
	digiMatches.GetYaxis().SetTitle('#')
	canvas.cd().SetLogy()
	digiMatches.SetLineWidth(3)
	digiMatches.SetLineColor(colorRwthDarkBlue)
	digiMatches.Draw()
	
	label = drawLabelCmsPrivateSimulation()
	
	canvas.Update()
	
	stats = digiMatches.GetListOfFunctions().FindObject("stats")
	stats.SetX1NDC(.7)
	stats.SetX2NDC(.9)
	stats.SetY1NDC(.75)
	stats.SetY2NDC(.9)
	
	canvas.Update()
	
	canvas.SaveAs('plots/controlPlots/digiMatchesPerDetId.pdf')
	canvas.SaveAs('plots/controlPlots/digiMatchesPerDetId.png')
	
	return canvas,digiMatches,label

def plotL1PerPt():
	ptValues = [0.,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,6.0,7.0,8.0,10.0,12.0,14.0,16.0,18.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,60.0,70.0,80.0,90.0,100.0,120.0,140.0,160]
	ptBins = [0]
	for i in range(len(ptValues)-1):
		ptBins.append( (ptValues[i]+ptValues[i+1])/2. )
	ptBins.append(2*ptValues[-1] - ptValues[-2])
	canvas = TCanvas('cL1PerPt')
	hist = TH1D('hist','# L1 per p_{T}',len(ptBins)-1,array('d',ptBins))
	chain = fileHandler.getTChain()
	eventCounter = 0
	liste = []
	nEvents = chain.GetEntries()
	for event in chain:
 		eventCounter += 1
		for l1 in event.l1MuonData:
			if not l1.pt in liste:
				liste.append(l1.pt)
 			hist.Fill(l1.pt)
 		if not eventCounter%10000:
 			printProgress(eventCounter,nEvents)
 		if eventCounter == 50000:
 			break
 	print
 	setupAxes(hist)
 	hist.SetStats(0)
 	hist.Scale(1,"width")
 	hist.Draw()
 	
 	label = drawLabelCmsPrivateSimulation()
   	
 	canvas.Update()
 	
#	print liste
	return hist, canvas, label

def plotEfficiencyCountCheck():
	c = TCanvas()
	genHist = fileHandler.getHistogram('hoMuonAnalyzer/count/Gen_Count')
	l1AndGenHist = fileHandler.getHistogram('hoMuonAnalyzer/count/GenAndL1Muon_Count')
	plusHoHist = fileHandler.getHistogram('hoMuonAnalyzer/count/GenAndL1MuonAndHoAboveThr_Count')
	plusHoHist.SetLineColor(colorRwthMagenta)
	genHist.SetLineColor(colorRwthDarkBlue)

	genHist.SetLineWidth(3)
	l1AndGenHist.SetLineWidth(3)
	plusHoHist.SetLineWidth(3)

	setPlotStyle()

	genHist.Draw()
	l1AndGenHist.Draw('same')
	plusHoHist.Draw('same')
	
	return c,l1AndGenHist,plusHoHist,genHist

output('Plotting digi matches per det id')
#res = plotHoDigiMatchesPerDetId()
output('Plot N L1 per Pt')
res2 = plotL1PerPt()
res3 = plotEfficiencyCountCheck()
raw_input('-->')
