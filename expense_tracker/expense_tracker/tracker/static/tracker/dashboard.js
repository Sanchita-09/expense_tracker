// ====== Dashboard Data ======
const chartsDiv = document.querySelector('.charts');

const TOTAL_INCOME = parseFloat(chartsDiv.dataset.income);
const TOTAL_EXPENSE = parseFloat(chartsDiv.dataset.expense);
const NET_INCOME = parseFloat(chartsDiv.dataset.net);
const MAX_INCOME = parseFloat(chartsDiv.dataset.maxIncome || TOTAL_INCOME);
const MIN_INCOME = parseFloat(chartsDiv.dataset.minIncome || 0);
const MAX_EXPENSE = parseFloat(chartsDiv.dataset.maxExpense || TOTAL_EXPENSE);
const MIN_EXPENSE = parseFloat(chartsDiv.dataset.minExpense || 0);

// ===== Colors =====

const categoryColors = {
    totalIncome: '#FFD700',   
    maxIncome: '#1E90FF',     
    minIncome: '#FF4500',     
    totalExpense: '#32CD32',  
    maxExpense: '#FF1493',    
    minExpense: '#8A2BE2',   
    net: '#00CED1'            
};


// ===== Pie Chart =====
const pieCtx = document.getElementById('pieChart').getContext('2d');
new Chart(pieCtx, {
    type: 'pie',
    data: {
        labels: [
            'Total Income',
            'Max Income',
            'Min Income',
            'Total Expense',
            'Max Expense',
            'Min Expense'
        ],
        datasets: [{
            data: [
                TOTAL_INCOME,
                MAX_INCOME,
                MIN_INCOME,
                TOTAL_EXPENSE,
                MAX_EXPENSE,
                MIN_EXPENSE
            ],
            backgroundColor: [
                categoryColors.totalIncome,
                categoryColors.maxIncome,
                categoryColors.minIncome,
                categoryColors.totalExpense,
                categoryColors.maxExpense,
                categoryColors.minExpense
            ],
            borderColor: '#fff',
            borderWidth: 2,
            hoverOffset: 20
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { 
                position: 'bottom',
                labels: { font: { size: 14 } }
            },
            tooltip: {
                callbacks: {
                    label: (context) => `${context.label}: ₹ ${context.raw.toLocaleString()}`
                }
            }
        },
        animation: { animateScale: true, animateRotate: true }
    }
});

// ===== Bar Chart =====
const barCtx = document.getElementById('barChart').getContext('2d');
new Chart(barCtx, {
    type: 'bar',
    data: {
        labels: [
            'Total Income',
            'Total Expense',
            'Net',
            'Max Income',
            'Min Income',
            'Max Expense',
            'Min Expense'
        ],
        datasets: [{
            label: 'Amount in ₹',
            data: [
                TOTAL_INCOME,
                TOTAL_EXPENSE,
                NET_INCOME,
                MAX_INCOME,
                MIN_INCOME,
                MAX_EXPENSE,
                MIN_EXPENSE
            ],
            backgroundColor: [
                categoryColors.totalIncome,
                categoryColors.totalExpense,
                categoryColors.net,
                categoryColors.maxIncome,
                categoryColors.minIncome,
                categoryColors.maxExpense,
                categoryColors.minExpense
            ],
            borderRadius: 12,
            borderSkipped: false
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true,
                grid: { color: '#ccc' },
                ticks: { callback: (value) => '₹ ' + value.toLocaleString(), color: '#222' }
            },
            x: {
                grid: { display: false },
                ticks: { color: '#222' }
            }
        },
        plugins: { legend: { display: false } },
        animation: { duration: 1500, easing: 'easeInOutQuart' }
    }
});

