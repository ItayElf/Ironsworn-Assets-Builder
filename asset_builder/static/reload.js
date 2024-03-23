const reload = async () => {
  const result = await fetch(window.location.href);
  const html = await result.text();

  document.querySelector("html").innerHTML = html;
};

setInterval(reload, 1000);
