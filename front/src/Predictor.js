import "./predictor.css";
import React, {useEffect, useState, CSSProperties} from "react";
import axios from "axios";
import HashLoader from "react-spinners/HashLoader";

const override: CSSProperties = {
    display: "block",
    position: "relative",
    left: "3px",
    top: "-60px",
    margin: "0 auto",
    borderColor: "red",
};



export function Predictor() {
    const [cResponse, setcResponse] = useState([]);
    const [getPCE, setGetPCE] = useState([]);
    // const [getmessage, setgetmessage] = useState([]);
    const [loading, setLoading] = useState(false);
    let [color, setColor] = useState("red");
    let [clicked, setClicked] = useState(false);
    
    const getRes = async () =>{
        const requestDict = {
            method : "GET",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch("http://127.0.0.1:8000/predict",requestDict);
        // 
        const data = await response.json();
        console.log(data);
        
        if(!response.ok) {console.log("response not working properly");}
        else{
            setcResponse(data);
        }
    }

    const form = document.getElementById("input_form");
    const responseF = (e) =>{
        e.preventDefault();
        setLoading(true);
        setClicked(true);
        const formData = new FormData(form);
        // console.log([...formData]);
        axios({
            method: "post",
            url: "http://127.0.0.1:8000/predict",
            data: [... formData]
        })
        .then((data) => {
            setGetPCE(data.data);
            // setgetmessage(data.message);
            setLoading(false);
            console.log(data.data);
        })
        .catch(function (err) {
            console.log(err);
        })
        
    }

    useEffect(() => {
        getRes();},[]);
       
    
    
    return(
            <div id="main_body">
                <h1 id="title">THE LC50<br/>
                VALUE<br/>
                PREDICTOR<br/> </h1>
            <div>
            
            
            <form id="input_form" onSubmit={responseF}>
            <br/>
            <br/>
            <div className="box">
            <h2 id="colName">CIC0 (in Unit)</h2>
<p id="limiter">Enter value between {cResponse.Cell_area_measured_numeric?.min} and {cResponse.Cell_area_measured_numeric?.max}</p>
<input type="number" name="Cell_area_measured_numeric" id="Cell_area_measured_numeric" className="text_box"  defaultValue = {cResponse.Cell_area_measured_numeric?.min} min={cResponse.Cell_area_measured_numeric?.min} max={cResponse.Cell_area_measured_numeric?.max} step = "0.0001" placeholder="0" required ></input>
           <h2 id="colName">SM1_Dz(Z) (in Unit)</h2>
<p id="limiter">Enter value between {cResponse.Cell_area_measured_numeric?.min} and {cResponse.Cell_area_measured_numeric?.max}</p>
<input type="number" name="Cell_area_measured_numeric" id="Cell_area_measured_numeric" className="text_box"  defaultValue = {cResponse.Cell_area_measured_numeric?.min} min={cResponse.Cell_area_measured_numeric?.min} max={cResponse.Cell_area_measured_numeric?.max} step = "0.0001" placeholder="0" required ></input>
            <h2 id="colName">GATS1i (in Unit)</h2>
<p id="limiter">Enter value between {cResponse.Cell_area_measured_numeric?.min} and {cResponse.Cell_area_measured_numeric?.max}</p>
<input type="number" name="Cell_area_measured_numeric" id="Cell_area_measured_numeric" className="text_box"  defaultValue = {cResponse.Cell_area_measured_numeric?.min} min={cResponse.Cell_area_measured_numeric?.min} max={cResponse.Cell_area_measured_numeric?.max} step = "0.0001" placeholder="0" required ></input>
            <h2 id="colName">NdsCH (in Unit)</h2>
<p id="limiter">Enter value between {cResponse.Cell_area_measured_numeric?.min} and {cResponse.Cell_area_measured_numeric?.max}</p>
<input type="number" name="Cell_area_measured_numeric" id="Cell_area_measured_numeric" className="text_box"  defaultValue = {cResponse.Cell_area_measured_numeric?.min} min={cResponse.Cell_area_measured_numeric?.min} max={cResponse.Cell_area_measured_numeric?.max} step = "0.0001" placeholder="0" required ></input>
            <h2 id="colName">NdssC (in Unit)</h2>
<p id="limiter">Enter value between {cResponse.Cell_area_measured_numeric?.min} and {cResponse.Cell_area_measured_numeric?.max}</p>
<input type="number" name="Cell_area_measured_numeric" id="Cell_area_measured_numeric" className="text_box"  defaultValue = {cResponse.Cell_area_measured_numeric?.min} min={cResponse.Cell_area_measured_numeric?.min} max={cResponse.Cell_area_measured_numeric?.max} step = "0.0001" placeholder="0" required ></input>
            <h2 id="colName">MLOGP (in Unit)</h2>
<p id="limiter">Enter value between {cResponse.Cell_area_measured_numeric?.min} and {cResponse.Cell_area_measured_numeric?.max}</p>
<input type="number" name="Cell_area_measured_numeric" id="Cell_area_measured_numeric" className="text_box"  defaultValue = {cResponse.Cell_area_measured_numeric?.min} min={cResponse.Cell_area_measured_numeric?.min} max={cResponse.Cell_area_measured_numeric?.max} step = "0.0001" placeholder="0" required ></input>
            </div>
               <br/>
               <br/>
               <br/>
                    <div id="submit_cover"><input type="submit" id="submit_btn" value="Predict" /></div>
                    <br/>
                    <br/>
                    <br/>
                    <div id= "result">
                    {/* <h2 id="result_text">{loading? "Predicting ...." : "" }</h2> */}
                    <h2 id="result_text">{clicked && !loading? "PREDICTED LC50 [-LOG(mol/L)] " : ""  }&emsp;</h2>
                    <div>
                    <h2 id="result_text_main">{loading? <HashLoader color={color} loading={loading} cssOverride={override} size={30} /> : getPCE.value }</h2>
                    </div>
                    <div> 
                    <br></br>
                    <br></br>
                    <div>{getPCE.value == 0.0 && !loading ? alert("Tune the Parameters Respective to Real Observation for Optimal Results"):  "" }</div>
                    </div>
                    </div>
                    </form>
                    </div>
            </div>
        );
    
};
