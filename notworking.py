if discrete == True:
      preypopulationsize = [entrysofsub['sizeprey']]
      predatorpopulationsize = [entrysofsub['predatorsize']]
      i = 0
      while i < entrysofsub['timeoflotvol']:
          integerindex = int(i//1)
          preypopulationsize.append(growthofprey*preypopulationsize[integerindex] - deathrateofprey*preypopulationsize[integerindex]*predatorpopulationsize[integerindex])
          predatorpopulationsize.append(-deathrateofpredator*predatorpopulationsize[integerindex] + growthofpredator*predatorpopulationsize[integerindex]*preypopulationsize[integerindex])
          i += entrysofsub['stepsoflotvol']
      app.stopSubWindow()
      app.setMessage('Solution', 'Prey: {0}\nPredator: {1}'.format(preypopulationsize[preypopulationsize.length - 1], predatorpopulationsize[predatorpopulationsize.length - 1]))
  else:
      preypopulationsize = [entrysofsub['sizeprey']]
      predatorpopulationsize = [entrysofsub['predatorsize']]
      i = 0
      while i < entrysofsub['timeoflotvol']:
          integerindex = int(i//1)
          preypopulationsize.append(entrysofsub['growthofprey']*preypopulationsize[integerindex] - entrysofsub['deathrateofprey']*preypopulationsize[integerindex]*predatorpopulationsize[integerindex])
          predatorpopulationsize.append(-entrysofsub['deathrateofpredator']*predatorpopulationsize[integerindex] + entrysofsub['growthofpredator']*predatorpopulationsize[integerindex]*preypopulationsize[integerindex])
          i += entrysofsub['stepsoflotvol']
