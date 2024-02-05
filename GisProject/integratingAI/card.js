const cardsData = [
    {
        title: 'По-добър мониторинг с данни в реално време',
        description: 'Компаниите могат да използват данни от ГИС, за да наблюдават промените в околната среда, причинени от техните дейности, като по този начин се оптимизира ефективността на работния процес.',
        imageUrl: '../homePage/images/Leonardo_Diffusion_XL_can_you_generate_me_a_symbol_for_renewab_0.jpg'
    },
    {
        title: 'Вземане на решения въз основа на данни',
        description: 'Платформите за ГИС осигуряват точен анализ на информацията за вземане на решения, основани на данни. Критичните бизнес процеси се подобряват, тъй като сега компаниите не разчитат на прогнози, а разполагат с богата геоинформация за дейността на своята индустрия. Това им позволява да постигат целите си по-бързо и да пестят средства. Освен за спестяване на разходи, ГИС са изключително полезни за автоматизиране на работните процеси и за намиране на по-безопасни зони. Компаниите могат да се възползват от намаленото оперативно и транспортно време, което намалява въглеродния отпечатък.',
        imageUrl: '../homePage/images/Leonardo_Diffusion_XL_can_you_generate_me_a_symbol_for_renewab_0.jpg'
    },
    {
        title: 'Подобрена оценка на терена ',
        description: 'Организациите могат по-добре да разбират отдалечените пространствени модели, които помагат при докладването и оценката. Системите за данни за управление на терени позволяват на компаниите за възобновяема енергия да планират маршрути за евакуация, да добиват природни ресурси и да прогнозират резултатите, за да спазват екологичните изисквания. Физическата същност на околната среда оказва влияние върху много оперативни изпълнения, така че е жизненоважно да се оцени правилно теренът, за да се намалят сметките и да се спести време.',
        imageUrl: '../homePage/images/Leonardo_Diffusion_XL_can_you_generate_me_a_symbol_for_renewab_0.jpg'
    },
    {
        title: "Оценка на жизнеспособността на мястото на проекта",
        description: "Информацията за местоположението може да помогне при оценката на способността на проектен обект да работи успешно. Анализът на геопространствени данни за енергийната индустрия дава много полезни сведения за възможните рискове и спецификата на работата в този или онзи район. Подробните географски данни позволяват на компаниите да предвидят рисковете и да се подготвят за възможните предизвикателства при функционирането на техните компании за възобновяеми енергийни източници.",
        imageUrl: '../homePage/images/Leonardo_Diffusion_XL_can_you_generate_me_a_symbol_for_renewab_0.jpg'        
    },
    {
        title: "Оптимизиране на проектирането и строителството",
        description: "ГИС елементите като карти, изображения и данни от дистанционни наблюдения могат да помогнат на компаниите при модернизирането на техните софтуерни функционалности. След като се има ясна представа за данните в реално време в района, може да се планира архитектурата и инфраструктурата на проекта по най-добрия начин, за да се осигурят устойчиви резултати.",
        imageUrl: '../homePage/images/Leonardo_Diffusion_XL_can_you_generate_me_a_symbol_for_renewab_0.jpg'        
    },
    {
        title: "Управление на енергийната мрежа",
        description: "С помощта на ГИС данни за възобновяемата енергия може да се постигне ефективно управление на енергийната мрежа. Картите позволяват да се моделират всички аспекти на проектната мрежа и да се генерира по-устойчива система.",
        imageUrl: '../homePage/images/Leonardo_Diffusion_XL_can_you_generate_me_a_symbol_for_renewab_0.jpg'        
    },
    {
        title: "Работни потоци в реално време",
        description: "ГИС осигуряват безпроблемен достъп до геоданни в реално време, които допринасят за ефективността на работните процеси. IoT сензорите (Изображение 1), заедно с подаването на данни в реално време, оптимизират начина, по който се  поддържат системите и се реагира на предизвикателства. Картографирането в реално време подобрява оперативната осведоменост и стандартите за безопасност.",
        imageUrl: '../homePage/images/Leonardo_Diffusion_XL_can_you_generate_me_a_symbol_for_renewab_0.jpg'        
    },
    {
        title: "Подобрена подкрепа за вземане на решения с изображения и дистанционно наблюдение",
        description: "Картите в устойчивата енергийна индустрия помагат за опазването на природните ресурси и околната среда чрез решения, основани на данни. Могат бързо да прогнозират потенциалното въздействие на своята дейност върху околната среда, за да предотвратят последствията. Растерният анализ, управлението на изображенията и мощните инструменти за визуализация ще спестят време и източници.",
        imageUrl: '../homePage/images/Leonardo_Diffusion_XL_can_you_generate_me_a_symbol_for_renewab_0.jpg'        
    },
    {
        title: "Оценяване на проекти за слънчева и вятърна енергия",
        description: "Методите на ВЕИ позволяват на проектите за устойчива енергия да работят ефективно, като използват търговски анализи. Днес ГИС и вятърната енергия, както и бизнесът с вода и слънчева енергия, са тясно свързани помежду си, защото анализът на данни позволява на компаниите да оценяват рисковете и рентабилността на проектите.",
        imageUrl: '../homePage/images/Leonardo_Diffusion_XL_can_you_generate_me_a_symbol_for_renewab_0.jpg'        
    }
];

function changeCardContent(index) {
    const card = document.querySelector(".card");
    card.classList.remove("fade-in-animation");

    document.querySelector("#current-card-index").textContent = index;
    document.querySelector(".images").src = cardsData[index].imageUrl;
    document.querySelector(".shown h5").textContent = cardsData[index].title;
    document.querySelector(".hidden p").textContent = cardsData[index].description;

    void card.offsetWidth;
    card.classList.add("fade-in-animation");
}


function incrementCard(e) {
    const currentIndex = Number(document.querySelector("#current-card-index").textContent) + 1 === cardsData.length ? 0 : Number(document.querySelector("#current-card-index").textContent) + 1;
    // console.log(currentIndex);
    
    changeCardContent(currentIndex);
}

function decrementCard(e) {
    const currentIndex = Number(document.querySelector("#current-card-index").textContent) - 1 < 0 ? cardsData.length - 1 : Number(document.querySelector("#current-card-index").textContent) - 1;    
    // console.log(currentIndex);

    changeCardContent(currentIndex);
}
