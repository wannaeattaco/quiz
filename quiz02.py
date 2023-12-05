"""You're a spellcrafter in an MMO. A job of a spellcrafter is to create new spells from runes. Don't worry too much about the runes.
You DO need to worry about the composition of spells and effects. Each spell consists of one or more effects,
each having a text (text) portion and a magnitude (mag) portion.

The problem: In a complex spell with multiple effects,
you have to determine how much you have to charge for putting together all the runes.
Normally, the price of a spell is the sum of magnitudes times number of different effects.
Also, sometimes there are cases where multiple effects with the same name are defined, which should be counted only one time.
For example, "restore health @ 30" and "restore health @ 40" should be counted as "restore health @ 70".

The class Effect has been implemented for you, but it is hidden.
Here is the documentation instead. You can expect that the Effect class will always perform as intended.
By the way, Effect when printed looks just like that: "{effect} @ {magnitude}"."""

class Effect:
    def __init__(self, text, mag):
        self.text = text
        self.mag = mag

    def get_text(self):
        return self.text

    def get_mag(self):
        return self.mag

    def __str__(self):
        return f'{self.text}@{self.mag}'


"""Spell works as follows:

The class is named Spell.
The class takes no initialization arguments. (HINT: You might still need to implement private attributes.)
The Spell must have the following methods:
add_effect(effect: Effect): adds an Effect to itself. The test code may reference to an existing Effect object. In which case, be careful about references.
change_effect_magnitude(index: int, newmag: int): for one effect specified by index (starting from 0), change its magnitude to newmag. The change affects this very specific instance of Effect in this spell only. Also, you must raise IndexError if index is out of range (etc.). For the purpose of this quiz, index input will always be int. You must also raise ValueError if newmag is less than or equal to 0.
The value of a Spell, accessible by the property called value, must return a value that is the sum of all Effect magnitudes multiplied by the number of unique Effect texts.
Two Spell objects must be comparable using the comparison operator. When comparing, compare only the values. For example, a Spell with only "restore health 60" is greater than a Spell with only "resurrect 40". If they're equal in value then they're equal.
The following doctest explains how the spell is managed and modified ...

"""

class Spell(Effect):

    ''' implements a spell
        >>> s = Spell()
        >>> s.add_effect(Effect('restore health', 40))
        >>> print(s)
        Spell: restore health @ 40, $40
        >>> s.add_effect(Effect('cure poison', 20))
        >>> print(s)
        Spell: restore health @ 40 + cure poison @ 20, $120
        >>> s.add_effect(Effect('restore health', 10))
        >>> print(s)
        Spell: restore health @ 40 + cure poison @ 20 + restore health @ 10, $140
        >>> s.change_effect_magnitude(2, 20)
        >>> print(s)
        Spell: restore health @ 40 + cure poison @ 20 + restore health @ 20, $160
    '''

    pass

    def __init__(self, effect, mag, text):
        super().__init__(text, mag)
        self.effect = effect
        self.mag = mag

    def add_effect(self, effect=Effect):
        self.effect = effect

    def change_effect_magnitude(self, index: int, newmag: int):
        if not isinstance(index, int):
            raise TypeError
        if newmag <= 0:
            raise ValueError

        if index > len(Effect):
            raise "index out of range"

    def get_value:


"""Also, you must implement another class called AreaSpell.

The class AreaSpell must be inherited from Spell. If you do not inherit properly there will be errors during test and you will not get full marks.

The arguments for initialization are as follows: (HINT: You might still need to implement other private attributes.)
radius: int ... required for init ... must be > 0
The value of an AreaSpell, is the same as Spell, but further multiplied by ((radius + 1)**1.4), THEN ROUNDED UP. (don't forget to import math)
The radius can be modified. You need to implement a getter and a setter.
AreaSpell and Spell are comparable using the value."""

class AreaSpell(Spell):
    ''' Implements an area-spell
        >>> e1 = Effect('buff def', 20)
        >>> e2 = Effect('buff atk', 10)
        >>> s1 = Spell()
        >>> s1.add_effect(e1)
        >>> s1.add_effect(e2)
        >>> s2 = AreaSpell(3)
        >>> s2.add_effect(e1)
        >>> s2.add_effect(e2)
        >>> print(s1)
        Spell: buff def @ 20 + buff atk @ 10, $60
        >>> print(s2)
        Spell: buff def @ 20 + buff atk @ 10, $418
        >>> s2.radius = 5
        >>> print(s2)
        Spell: buff def @ 20 + buff atk @ 10, $738
    '''
    pass

