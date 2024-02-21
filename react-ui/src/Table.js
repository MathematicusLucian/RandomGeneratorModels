
import * as React from "react";
import { CompactTable } from "@table-library/react-table-library/compact";
import { useTheme } from "@table-library/react-table-library/theme";
import { getTheme } from "@table-library/react-table-library/baseline";

const Table = (props) => {

    if(props.data != "Loading . . .") {
        const chartData = JSON.parse(props.data);
        const entries = Object.entries(chartData);
        let i = 0;
        const data = entries.map( ([modelName, details]) => {
            let modelJson = {"id": i, "model": modelName};
            Object.entries(details).map( ([iterationLevel, val]) => {
                return modelJson[iterationLevel] = val["avg"];
            });
            i++;
            return modelJson;
        });

        console.log('entries', JSON.stringify(data));

        const nodes = [{"10":0.11333048343658447,"100":0.09228651523590088,"1000":0.09561753273010254,"10000":0.08213450908660888,"id":0,"model":"Arg Max"},{"10":0.03723549842834473,"100":0.020389437675476074,"1000":0.0298095703125,"10000":0.019308805465698242,"id":1,"model":"Basic"},{"10":0.021104264259338378,"100":0.024357295036315917,"1000":0.020333147048950194,"10000":0.020894575119018554,"id":2,"model":"Binary Search"},{"10":0.09020447731018066,"100":0.07023792266845703,"1000":0.07863841056823731,"10000":0.072220778465271,"id":3,"model":"Numpy B Search wv EH"},{"10":0.08176672458648682,"100":0.06819784641265869,"1000":0.06730847358703614,"10000":0.08190431594848632,"id":4,"model":"Numpy Binary Search"},{"10":0.05444214344024658,"100":0.04854292869567871,"1000":0.05663292407989502,"10000":0.04255526065826416,"id":5,"model":"Random Choices"},{"10":0.024190711975097656,"100":0.02208881378173828,"1000":0.02592325210571289,"10000":0.018039941787719727,"id":6,"model":"Zip"}];

        const dataX = { nodes };

        console.log('dataX', dataX);
        console.log('dataX', typeof dataX);

        const theme = useTheme([
            getTheme(),
            {
            HeaderRow: `
                background-color: #eaf5fd;
            `,
            Row: `
                &:nth-of-type(odd) {
                background-color: #d2e9fb;
                }
                &:nth-of-type(even) {
                background-color: #eaf5fd;  
                }
            `,
            },
        ]);

        const COLUMNS = [
            { label: "Model Name", renderCell: (item) => item.model },
            { label: "10", renderCell: (item) => item["10"] },
            { label: "100", renderCell: (item) => item["100"] },
            { label: "1000", renderCell: (item) => item["1000"] },
            { label: "10000", renderCell: (item) => item["10000"] }
        ];

        return (
            <>
            <CompactTable columns={COLUMNS} data={dataX} theme={theme} />
            </>
        );
    }
};

export default Table;