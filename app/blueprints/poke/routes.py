from flask import request, flash, redirect, url_for, render_template
from flask_login import current_user
from . import poke
from .forms import PokeForm
from app.models import Poke
from app import db


@poke.route('/create_pokemon', methods=['GET', 'POST'])
def create_pokemon():
    form = PokeForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Data coming from the PokeForm
        poke_data = {
            'img_url': form.img_url.data,
            'poke_name': form.poke_name.data,
            'ability': form.ability.data,
            'base_experience': form.base_experience.data,
            'hp': form.hp.data,
            'attack': form.attack.data,
            'defense': form.defense.data,
            'user_id': current_user.id
        }

        # Create Poke Instance
        print('Creating Instance')
        new_pokemon = Poke()

        print(new_pokemon.id)
        # Set poke_data to our Poke attributes
        print('Unpacking')
        new_pokemon.from_dict(poke_data)

        # Save to our database
        db.session.add(new_pokemon)
        db.session.commit()

        flash('Successfully created your Pokemon!', 'success')
        return redirect(url_for('main.home'))
    else:
        return render_template('create_pokemon.html', form=form)
