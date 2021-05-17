function download() {
  const country = document.getElementById("updateForm").elements[0].value;
  const from = document.getElementById("updateForm").elements[1].value;
  const to = document.getElementById("updateForm").elements[2].value;
  const total = document.getElementById("updateForm").elements[4].checked ? 1 : 0;
  const active = document.getElementById("updateForm").elements[5].checked ? 1 : 0;
  const deaths = document.getElementById("updateForm").elements[6].checked ? 1 : 0;
  const recoveries = document.getElementById("updateForm").elements[7].checked ? 1 : 0;

  var link = document.createElement("a");
  link.href = `http://localhost:8080/download/${country}/${from}/${to}/${total}${active}${deaths}${recoveries}`;
  link.click();
  link.remove();
}
