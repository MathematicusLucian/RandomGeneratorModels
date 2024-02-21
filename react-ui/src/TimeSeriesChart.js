import React from 'react';
import "./timeSeriesChart.css";
import { ResponsiveLine } from '@nivo/line'

const TimeSeriesChart = (props) => {

    if(props.data != "Loading . . .") {
        const chartData = JSON.parse(props.data);
        const entries = Object.entries(chartData);
        const data = [];
        entries.map( ([modelName, details]) => {
            let modelJson = {"id": modelName, "color": "", "data":[]};
            Object.entries(details).map( ([iterationLevel, val]) => {
                return modelJson["data"].push({ "x": iterationLevel, "y": val["avg"]});
            });
            data.push(modelJson);
        });

        return (        
            <div id="chartWrapper">
                <ResponsiveLine
                    data={ data }
                    margin={{ top: 50, right: 150, bottom: 50, left: 60 }}
                    xScale={{ type: 'point' }}
                    yScale={{
                        type: 'linear',
                        min: 'auto',
                        max: 'auto',
                        stacked: true,
                        reverse: false
                    }}
                    yFormat=" >-.2f"
                    axisTop={null}
                    axisRight={null}
                    axisBottom={{
                        tickSize: 5,
                        tickPadding: 5,
                        tickRotation: 0,
                        legend: 'Iteration Levels',
                        legendOffset: 36,
                        legendPosition: 'middle',
                        truncateTickAt: 0
                    }}
                    axisLeft={{
                        tickSize: 5,
                        tickPadding: 5,
                        tickRotation: 0,
                        legend: 'Execution Time (Minutes:Seconds)',
                        legendOffset: -40,
                        legendPosition: 'middle',
                        truncateTickAt: 0
                    }}
                    colors={{ scheme: 'pastel1' }}
                    pointSize={10}
                    pointColor={{ theme: 'background' }}
                    pointBorderWidth={2}
                    pointBorderColor={{ from: 'serieColor' }}
                    pointLabelYOffset={-12}
                    useMesh={ true }
                    legends={[
                        {
                            anchor: 'bottom-right',
                            direction: 'column',
                            justify: false,
                            translateX: 155,
                            translateY: 0,
                            itemsSpacing: 0,
                            itemDirection: 'right-to-left',
                            itemWidth: 110,
                            itemHeight: 30,
                            itemOpacity: 1,
                            symbolSize: 12,
                            symbolShape: 'circle',
                            symbolBorderColor: 'rgba(0, 0, 0, .8)',
                            textColor: '#fff',
                            textSize: '20px',
                            effects: [
                                {
                                    on: 'hover',
                                    style: {
                                        itemBackground: 'rgba(0, 0, 0, .03)',
                                        itemOpacity: 1
                                    }
                                }
                            ]
                        }
                    ]}
                    textFill="#fff"
                />
            </div>
        );
    } else {
        return (<></>);
    }
}

export default TimeSeriesChart;