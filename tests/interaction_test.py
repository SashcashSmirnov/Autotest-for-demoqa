import time
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


class TestInteractions:

    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after
            assert grid_before != grid_after

    class TestSelectablePage:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(
                driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            grid_list = selectable_page.select_grid_item()
            assert len(item_list) > 0
            assert len(grid_list) > 0

    class TestResizable:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(
                driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert (
                '500px', '300px') == max_box, "maximum size not equal to '500px', '300px'"
            assert (
                '150px', '150px') == min_box, "minimum size not equal to '150px', '150px'"
            assert min_resize != max_resize, "size has not been changed"


class TestDroppablePage:

    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        text = droppable_page.drop_simple()
        assert text == 'Dropped!'

    def test_accept_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        not_accept, accept = droppable_page.drop_accept()
        assert not_accept == 'Drop here'
        assert accept == 'Dropped!'

    def test_prevent_propogation_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
        assert not_greedy == 'Dropped!'
        assert not_greedy_inner == 'Dropped!'
        assert greedy == 'Outer droppable'
        assert greedy_inner == 'Dropped!'

    def test_revert_draggable_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        position_after_move, position_after_revert = droppable_page.drop_will_revert_draggable()
        position_after_move_not_revert, position_after_revert_not_revert = droppable_page.drop_will_not_revert_draggable()
        assert position_after_move != position_after_revert
        assert position_after_move_not_revert == position_after_revert_not_revert


class TestDraggablePage:

    def test_simple_draggable(self, driver):
        draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
        draggable_page.open()
        before, after = draggable_page.simple_drag_box()
        assert before != after

    def test_axis_restricted_draggable(self, driver):
        draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
        draggable_page.open()
        top_x, left_x = draggable_page.axis_restricted_x()
        top_y, left_y = draggable_page.axis_restricted_y()
        assert top_x[0][0] == top_x[1][0] and int(
            top_x[1][0]) == 0, "box position has not changed or there has been a shift in the y-axis"
        assert left_x[0][0] != left_x[1][0] and int(
            left_x[1][0]) != 0, "box position has not changed or there has been a shift in the y-axis"
        assert top_y[0][0] != top_y[1][0] and int(
            top_y[1][0]) != 0, "box position has not changed or there has been a shift in the x-axis"
        assert left_y[0][0] == left_y[1][0] and int(
            left_y[1][0]) == 0, "box position has not changed or there has been a shift in the x-axis"
