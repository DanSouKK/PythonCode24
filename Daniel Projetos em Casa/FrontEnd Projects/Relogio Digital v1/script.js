// Função simplificada de seleção de elemento
const $ = (selector) => {
    return document.querySelector(selector);
}

// Seleção dos elementos principais do relógio
const hour = $('.hour');
const dot = $('.dot');
const min = $('.min');
const week = $('.week');

// Variável para controlar pisca dos dois pontos
let showDot = true;

// Função principal de atualização do relógio
function update() {
    // Alterna estado dos dois pontos
    showDot = !showDot;
    const now = new Date();

    // Aplicar/remover classe de invisibilidade nos dois pontos
    if (showDot) {
        dot.classList.add('invisible');
    } else {
        dot.classList.remove('invisible');
    }

    // Atualizar hora e minutos com formatação de dois dígitos
    hour.textContent = now.getHours().toString().padStart(2, '0');
    min.textContent = now.getMinutes().toString().padStart(2, '0');

    // Remover destaque de todos os dias
    Array.from(week.children).forEach((ele) => {
        ele.classList.remove('active');
    });

    // Adicionar destaque para o dia atual
    week.children[now.getDay()].classList.add('active');
}

// Atualizar o relógio a cada 500 milissegundos
setInterval(update, 500);