import pytest
import svcards

DS_RESULT = 'Dimension Shift, [Spell], Cost: 18, "Gain an extra turn after this one.<br>Subtract 0 from the cost of this card.<br>Spellboost: Subtract 1 more."'

def test_get_cards():
    card_data = svcards.get_cards()
    assert isinstance(card_data, list)
    assert len(card_data) > 0

def test_find_index():
    find = svcards.find_index
    assert find('gob','goblin') == 0
    assert find('Tia','Crystalia Tia') == 10
    assert find('T','oot') == 2
    assert find('p','xxP') == 2

def test_create_cards():
    assert svcards.create_cards

def test_search_cards():
    results = []
    search = svcards.search_cards('shift', lambda n: results.append(n))
    svcards.search_cards('Tia', lambda n: results.append(n))
    tia_result = "Crystalia Tia, [Minion]"
    assert search == None
    assert results[0] == DS_RESULT
    assert results[1][:len(tia_result)] == tia_result
    