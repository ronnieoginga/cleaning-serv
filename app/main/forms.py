from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Cleaning area',validators=[Required()])
    content = StringField('Your adress',validators=[Required()])
    category = SelectField('Category', choices=[('Choose Category', 'Choose Category'),('Temporary', 'Temporary'),('Part-time', 'Part-time'),('Parmanent', 'Parmanent')])
    review = TextAreaField('Contacts', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please, tell us something about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')
