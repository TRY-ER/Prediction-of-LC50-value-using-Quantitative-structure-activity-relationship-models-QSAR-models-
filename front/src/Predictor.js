import "./predictor.css";
import React, { useEffect, useState, CSSProperties } from "react";
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

    const getRes = async () => {
        const requestDict = {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        };
        const response = await fetch("http://127.0.0.1:8000/predict", requestDict);
        // 
        const data = await response.json();
        console.log(data);

        if (!response.ok) {
            console.log("response not working properly");
        }
        else {
            setcResponse(data);
        }
    }

    const form = document.getElementById("input_form");
    const responseF = (e) => {
        e.preventDefault();
        setLoading(true);
        setClicked(true);
        const formData = new FormData(form);
        console.log("formdata",[...formData]);
        axios.post("http://127.0.0.1:8000/predict"
            , {
                "value": [...formData]
            }
        )
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
        getRes();
    }, []);



    return (
        <div id="main_body">
            <h1 id="title">THE LC50<br />
                VALUE<br />
                PREDICTOR<br /> </h1>
            <div>


                <form id="input_form" onSubmit={responseF}>
                    <br />
                    <br />
                    <div className="box">
                        <h2 id="colName">CIC0 (in Unit)</h2>
                        <p id="limiter">Enter value between {cResponse.CIC0?.min} and {cResponse.CIC0?.max}</p>
                        <input type="number" name="CIC0" id="CIC0" className="text_box" defaultValue={cResponse.CIC0?.min} min={cResponse.CIC0?.min} max={cResponse.CIC0?.max} step="0.0001" placeholder="0" required ></input>
                        <h2 id="colName">SM1_Dz(Z) (in Unit)</h2>
                        <p id="limiter">Enter value between {cResponse.SM1_Dz?.min} and {cResponse.SM1_Dz?.max}</p>
                        <input type="number" name="SM1_Dz" id="SM1_Dz" className="text_box" defaultValue={cResponse.SM1_Dz?.min} min={cResponse.SM1_Dz?.min} max={cResponse.SM1_Dz?.max} step="0.0001" placeholder="0" required ></input>
                        <h2 id="colName">GATS1i (in Unit)</h2>
                        <p id="limiter">Enter value between {cResponse.GATS1i?.min} and {cResponse.GATS1i?.max}</p>
                        <input type="number" name="GATS1i" id="GATS1i" className="text_box" defaultValue={cResponse.GATS1i?.min} min={cResponse.GATS1i?.min} max={cResponse.GATS1i?.max} step="0.0001" placeholder="0" required ></input>
                        <h2 id="colName">NdsCH (in Unit)</h2>
                        <p id="limiter">Enter value between {cResponse.NdsCH?.min} and {cResponse.NdsCH?.max}</p>
                        <input type="number" name="NdsCH" id="NdsCH" className="text_box" defaultValue={cResponse.NdsCH?.min} min={cResponse.NdsCH?.min} max={cResponse.NdsCH?.max} step="0.0001" placeholder="0" required ></input>
                        <h2 id="colName">NdssC (in Unit)</h2>
                        <p id="limiter">Enter value between {cResponse.NdssC?.min} and {cResponse.NdssC?.max}</p>
                        <input type="number" name="NdssC" id="NdssC" className="text_box" defaultValue={cResponse.NdssC?.min} min={cResponse.NdssC?.min} max={cResponse.NdssC?.max} step="0.0001" placeholder="0" required ></input>
                        <h2 id="colName">MLOGP (in Unit)</h2>
                        <p id="limiter">Enter value between {cResponse.MLOGP?.min} and {cResponse.MLOGP?.max}</p>
                        <input type="number" name="MLOGP" id="MLOGP" className="text_box" defaultValue={cResponse.MLOGP?.min} min={cResponse.MLOGP?.min} max={cResponse.MLOGP?.max} step="0.0001" placeholder="0" required ></input>
                    </div>
                    <br />
                    <br />
                    <br />
                    <div id="submit_cover"><input type="submit" id="submit_btn" value="Predict" /></div>
                    <br />
                    <br />
                    <br />
                    <div id="result">
                        {/* <h2 id="result_text">{loading? "Predicting ...." : "" }</h2> */}
                        <h2 id="result_text">{clicked && !loading ? "PREDICTED LC50 [-LOG(mol/L)] " : ""}&emsp;</h2>
                        <div>
                            <h2 id="result_text_main">{loading ? <HashLoader color={color} loading={loading} cssOverride={override} size={30} /> : getPCE.value}</h2>
                        </div>
                        <div>
                            <br></br>
                            <br></br>
                            <div>{getPCE.value == 0.0 && !loading ? alert("Tune the Parameters Respective to Real Observation for Optimal Results") : ""}</div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    );

};
