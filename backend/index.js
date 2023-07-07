import express from "express";
import morgan from "morgan";
import cors from "cors";
import fs from "fs";

const app = express();

app.use(express.json());
app.use(morgan("dev"));
app.use(cors());

app.post("/item", (req, res) => {
	const item = req.body.item;
	fs.readFile("items.json", (err, data) => {
        console.log(data);
		let json = JSON.parse(data);
        let size = Object.keys(json).length;
        json[`item-${size+1}`] = item;
        console.log(json);

		fs.writeFile("items.json", JSON.stringify(json), err => {
            if (err) throw err;
        });
	});
	res.status(200).send({status: "ok"});
});

app.listen(5000, console.log("Server running on port 5000"));
