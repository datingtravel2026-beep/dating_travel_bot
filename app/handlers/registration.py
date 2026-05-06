from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from app.states.registration import Registration
from app.database.queries import update_user
from app.keyboards.registration import gender_kb, confirm_kb
from app.keyboards.main_menu import main_menu

router = Router()


@router.message(lambda m: m.text == "Начать")
async def reg_start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer("Введите имя")


@router.message(Registration.name)
async def reg_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.age)
    await message.answer("Введите возраст")


@router.message(Registration.age)
async def reg_age(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await state.set_state(Registration.gender)
    await message.answer("Выберите пол", reply_markup=gender_kb())


@router.message(Registration.gender)
async def reg_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Registration.looking_for)
    await message.answer("Кого ищете?")


@router.message(Registration.looking_for)
async def reg_looking(message: types.Message, state: FSMContext):
    await state.update_data(looking_for=message.text)
    await state.set_state(Registration.city)
    await message.answer("Введите город")


@router.message(Registration.city)
async def reg_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Registration.photo)
    await message.answer("Отправьте фото")


@router.message(Registration.photo)
async def reg_photo(message: types.Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(photo_id=photo_id)

    data = await state.get_data()

    text = (
        f"Имя: {data['name']}\n"
        f"Возраст: {data['age']}\n"
        f"Пол: {data['gender']}\n"
        f"Ищу: {data['looking_for']}\n"
        f"Город: {data['city']}"
    )

    await state.set_state(Registration.confirm)
    await message.answer_photo(photo_id, caption=text, reply_markup=confirm_kb())


@router.message(Registration.confirm)
async def reg_confirm(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        data = await state.get_data()

        await update_user(
            message.from_user.id,
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            looking_for=data["looking_for"],
            city=data["city"],
            photo_id=data["photo_id"],
            is_registered=True
        )

        await state.clear()
        await message.answer("Анкета создана!", reply_markup=main_menu())
