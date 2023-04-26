document.addEventListener("DOMContentLoaded", () => {
    var enter = (<HTMLInputElement>document.getElementById("enter"));

    enter.onclick = () => {
        (async () => {
            let input = (<HTMLInputElement>document.getElementById("input")).value;
            const req = await fetch('/api/webscraper/parse', {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    url: input
                })
            });
            if (req.status !== 200) {
                console.log(req.status);
                return;
            }
            const res = await req.json();
            console.log(res['words']);
            console.log(res['trendMean']);
        })();
    };
});