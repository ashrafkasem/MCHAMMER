#!/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('scripts', metavar='scripts', type=str, nargs='+',
                   help='The subscript(s) to be called for plotting')

parser.add_argument('--data','-d'
					,dest='data'
					,action="store_true",default=False
					,help='Skip anything that has to do with GEN')

parser.add_argument('--list','-l'
					,dest='list'
					,action="store_true",default=False
					,help='Show list of available scripts')

parser.add_argument('--source','-s'
					,dest='source'
					,help='File name scheme for the source of events')

parser.add_argument('--DEBUG'
					,dest='DEBUG',action="store_true",default=False
					,help='Enable more verbose output in modules.')

args = parser.parse_args()

from comparison.Comparison import Comparison
from dataQuality.ControlPlots import ControlPlots
from dataQuality.Energy	import Energy
from dataQuality.EvsEtaPhi import EvsEtaPhi
from phishift.DeltaPhi import DeltaPhi
from efficiency.Counters import Counters
from efficiency.GridMatching import GridMatching
from efficiency.HoThresholdScan import HoThresholdScan 
from efficiency.TimeWindow import TimeWindow
from dataQuality.PtResolution import PtResolution
from dataQuality.QualityCode import QualityCode
from dataQuality.Timing import Timing

def plotTiming():
	lib = Timing(filename=args.source,data=args.data,debug = args.DEBUG)
	resDtCoordsWrong = lib.plotDtBxWrongCoordinates()
	#resHoTimeEta = lib.plotHoTimeVsEta()
	resEvsTime = lib.plotHoEnergyVsTime()
	resDeltaTime = lib.plotDeltaTime()
	resBxId = lib.plotL1BxId()
	resTightBxId = lib.plotL1BxId(tight=True)
	resTimeHo = lib.plotMatchedHoTime()
	res = lib.plotHoTime()
	res6 = lib.plotHoTimeLog()
	res4 = lib.plotImprovementInDt()
	if not args.data:
		lib.plotEtaOfWrongBxId()
		lib.plotEtaPhiOfWrongBxId()
		lib.plotFractionsOfBxId()
		res2 = lib.plotDetectorContributionsToTiming()
		res5 = lib.plotPtAndPhiOfWrongBxId()
		res4 = lib.plotImprovementInDt()
		res3 = lib.plotPtAndEtaOfWrongBxId()
	raw_input('-->')
	return

def plotEVsEtaPhi():
	lib = EvsEtaPhi(filename = args.source, data=args.data,debug = args.DEBUG)
	lib.calculateCentralFractionInTight()
	reseMaxCountsTight = lib.plotEMaxCountsForTightMuons()
	reseMaxCounts = lib.plotEMaxCounts()
	res = lib.plotAverageEnergyAroundL1()
	res2 = lib.plotAverageEMaxAroundL1()
	res3 = lib.plot1DEnergyAroundL1()
	res4 = lib.plot1DEMaxAroundL1()
	res5 = lib.compareHistogramMethods()
	res6 = lib.plotEavForTightMuons()
	res7 = lib.plotEavPerWheelForTightMuons()
	resWheelwise = lib.plotEAveragePerWheel()
	resEtaPhiTight = lib.plotEtaPhiForTightL1()
	raw_input('-->')
	return

def plotControlPlots():
	plots = ControlPlots(filename=args.source,data=args.data,debug = args.DEBUG)
	res1 = plots.plotL1PerPt()
	res2 = plots.plotHoIEtaIPhi()
	res3 = plots.plotHoEtaPhiMatchedToL1()
	resTightAndHoIetaIphi = plots.plotHoIEtaIPhiMatchedToTightL1()
	resL1AndHoIetaIphi = plots.plotHoIEtaIPhiMatchedToL1()
	resPatTightHoEtaPhi = plots.plotHoEtaPhiMatchedToTightL1()
	resSameScale = plots.plotIEtaIPhiOnSameScales()
	resL1Multiplicity = plots.plotL1PresentMultiplicity()
	#res2 = plots.plotHoDigiMatchesPerDetId()
	if not args.data:
		res4 = plots.plotEfficiencyCountCheck()
		res5 = plots.plotGenEtaPhi()
	raw_input('-->')
	return

def plotTimeWindow():
	lib = TimeWindow(filename=args.source,data=args.data,debug = args.DEBUG)
	resAllL1 = lib.plotAllL1Together()
	resBxidFail = lib.plotBxidVsPtFails()
	resBxidSucc = lib.plotBxidVsPtMatch()
	if not args.data:
		resTimeWindowAlone = lib.plotTimeWindowAlone()
		resTruthL1 = lib.plotTruthL1Together()
	raw_input('-->')
	return

def plotPtResolution():
	#  		libTruth = PtResolution(filename=args.source,truth=True,data=args.data,debug = args.DEBUG)
#  		resTruth4 = libTruth.plotL1()
#  		resTruth5 = libTruth.plotL1Tight()
#  		resTruth6 = libTruth.plotL1AndHo()
#  		resTruth7 = libTruth.plotL1TightAndHo()
#  		resTruth8 = libTruth.plotL1NotHo()
#  		resTruth9 = libTruth.plotL1TightNotHo()
#  		resTruth1 = libTruth.plotPtResolutionHistograms()
#  		resTruth2 = libTruth.plotTightPtResolution()
#  		resTruth3 = libTruth.plotLoosePtResolution()
# 		raw_input('Hit return to continue')
	lib = PtResolution(filename=args.source,truth=False,data=args.data,debug = args.DEBUG)
	res4 = lib.plotL1()
	res5 = lib.plotL1Tight()
	res6 = lib.plotL1AndHo()
	res7 = lib.plotL1TightAndHo()
	res8 = lib.plotL1NotHo()
	res9 = lib.plotL1TightNotHo()
	res1 = lib.plotPtResolutionHistograms()
	res2 = lib.plotTightPtResolution()
	res3 = lib.plotLoosePtResolution()
	raw_input('-->')
	return

def plotQualityCodes():
	lib = QualityCode(filename=args.source,data=args.data,debug = args.DEBUG)
	res1 = lib.plot3x3MatchQualityCodesVsPt()
	res2 = lib.plot3x3FailQualityCodesVsPt()
	res3 = lib.plotQualityCodesStacked(1)
	res4 = lib.plotAllQualitiyCodes()
	raw_input('-->')
	return

def plotCounters():
	lib = Counters(filename=args.source,data=args.data,debug = args.DEBUG)
	res = lib.plotL1AndTightL1Counters()
	res2 = lib.plotTightL1EtaPhiRatio()
	raw_input('-->')
	return

def plotThresholdScan():
	lib = HoThresholdScan(filename=args.source,data=args.data,debug = args.DEBUG)
	res = lib.plotHoThresholdScan()
	raw_input('-->')
	return

def plotEfficiency():
	lib = GridMatching(filename=args.source, data=args.data,debug = args.DEBUG)
	#res = lib.plotL1GridMatchingEfficiency()
	res2 = lib.plotL13x3AndL1Tight3x3()
	res3 = lib.plotL13x3AndL1Tight3x3L1Coordinates()
	res4 = lib.plotL13x3AndL1Tight3x3FromPatL1Pt()
	res5 = lib.plotL13x3AndL1Tight3x3FromPat()
	c = ROOT.TCanvas('123','asdf')
	c.cd()
	res2[3].SetMarkerStyle(23)
	temp = res3[3].Draw()
	temp2 = res4[3].Draw('same')
	c.Update()
	if not args.data:
		resL1Truth = lib.plotL1TruthGridMatchingPlot()
		res3x3Together = lib.plot3x3GridTogether()
		resN3x3 = lib.plotNtotalGridMatching3x3()
		res5x5Together = lib.plot5x5GridTogether()
	raw_input('-->')
	return

def plotEnergy():
	lib = Energy(filename = args.source, data = args.data,debug = args.DEBUG)
	resEnergy = lib.plotEnergy()
	resEnergyNorm = lib.plotEnergyNormalized()
	resMipNorm = lib.plotEnergyNormalizedToMip()
	resEPerWheelHo = lib.plotHoEnergyPerWheel()
	resEPerWheelMatchedHo = lib.plotMatchedHoEnergyPerWheel()
	resEPerWheelTogether = lib.plotMatchedAndNotMatchedPerWheel()
	raw_input('-->')
	return

def plotCompareEnergy():
	libComparison = Comparison(data = args.data,debug = args.DEBUG)
	resL1Count = libComparison.compareL1Count()
	resEPerWheel = libComparison.compareEnergyPerWheel()
	resEAbsolute = libComparison.compareEnergyAbsolute()
	resEAbsoluteMatched = libComparison.compareEnergyAbsoluteHoMatched()
	resEIntegralNorm = libComparison.compareEnergyNormalizedToIntegral()
	resEIntegralNormTight = libComparison.compareEnergyTightNormalizedToIntegral()
	raw_input('-->')
	
	return

def plotPhiShift():
	lib = DeltaPhi(filename = args.source,data=args.data,debug = args.DEBUG)
	resDeltaPhi = lib.plotDeltaPhiHistogram()
	resEta = lib.plotDeltaPhiVsL1Eta()
	resdPhiVsPtL1 = lib.plotDeltaPhiVsL1Pt()
	resdPhiVsPtL1Tight = lib.plotDeltaPhiVsL1TightPt()
	resAllEtaPhi = lib.plotEtaPhiForAllL1()
	resEtaPhiMap = lib.plotEtaPhiForDeltaPhiOne()
	if not args.data:
		#res3 = lib.plotDeltaPhiVsGenPt()
		res4 = lib.plotL1PhiVsHoPhi()
		res5 = lib.plotL1PhiVsHoIPhi()
		#res = lib.plotDeltaPhiVsL1Phi()
		#res2 = lib.plotDeltaPhiVsL1Pt()
	raw_input('-->')
	return

from ROOT import gROOT
import ROOT
print ROOT.__file__
gROOT.ProcessLine(".L $HOMUONTRIGGER_BASE/python/loader.C+");

scripts = ['controlPlots','eVsEtaPhi','timeWindow','ptResolution','qualityCodes',
			'counters','thresholdScan','efficiency','energy','compareEnergy','timing','phiShift']

for script in args.scripts:
	if(script == 'controlPlots'):
		plotControlPlots()
	elif(script == 'eVsEtaPhi'):
		plotEVsEtaPhi()
	elif(script == 'phiShift'):
		plotPhiShift()
	elif(script == 'timeWindow'):
		plotTimeWindow()
	elif(script == 'ptResolution'):
		plotPtResolution()
	elif(script == 'qualityCodes'):
		plotQualityCodes()
	elif (script=='timing'):
		plotTiming()
	elif (script == 'counters'):
		plotCounters()
	elif (script == 'thresholdScan'):
		plotThresholdScan()
	elif (script == 'efficiency'):
		plotEfficiency()
	elif (script == 'energy'):
		plotEnergy()
	elif (script == 'comparison'):
		plotCompareEnergy()
	else:
		print 'Unknown script requested: %s' % (script)
		print "Available Scripts:"
		for script in scripts:
			print '\t',script
			
