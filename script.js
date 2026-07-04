const form = document.getElementById("jobForm");

form.addEventListener("submit", async function (e) {
  e.preventDefault();
  console.log(document.getElementById("birthdate"));
  console.log(document.getElementById("phone"));
  console.log(document.getElementById("degree"));
  console.log(document.getElementById("description"));
  const data = {
    first_name: document.getElementById("first-name").value,
    last_name: document.getElementById("last-name").value,
    national_id: document.getElementById("national-id").value,
    birthdate: document.getElementById("birthdate").value,
    gender: document.querySelector('input[name="gender"]:checked')?.id,
    email: document.getElementById("gmail").value,
    phone: document.getElementById("phone").value,
    website: document.getElementById("address").value,
    degree: document.getElementById("degree").value,
    newsletter: document.getElementById("newsletter").checked,
    description: document.getElementById("description").value,
  };

    const response = await fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  const result = await response.json();

  alert(result.message);
});
