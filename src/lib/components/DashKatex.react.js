import React, {Component} from 'react';
import PropTypes from 'prop-types';
import 'katex/dist/katex.min.css';
import katex from 'katex';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class DashKatex extends Component {
    constructor(props) {
        super(props);
    }

    renderKatex() {
        const {
            expression,
            throwOnError,
            displayMode,
            errorColor,
            macros
        } = this.props;

        const {katexElement} = this.refs;

        katex.render(expression, katexElement, {
            throwOnError,
            displayMode,
            errorColor,
            macros
        });
    }


    componentDidUpdate() {
        this.renderKatex();
    }

    componentDidMount() {
        this.renderKatex();
    }

    render() {
        return (
            <div ref="katexElement"/>
        );
    }
}

DashKatex.defaultProps = {
    displayMode: false,
    throwOnError: true,
    errorColor: '#cc0000',
};

DashKatex.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,

    /**
     * Expression to be rendered
     */
    expression: PropTypes.string,

    /**
     * If true the math will be rendered in display mode, which will put the
     * math in display style (so \int and \sum are large, for example), and
     * will center the math on the page on its own line. If false the math
     * will be rendered in inline mode. (default: false)
     */
    displayMode: PropTypes.bool,

    /**
     * If true (the default), KaTeX will throw a ParseError when it encounters
     * an unsupported command or invalid LaTeX. If false, KaTeX will render
     * unsupported commands as text, and render invalid LaTeX as its source
     * code with hover text giving the error, in the color given by errorColor.
     */
    throwOnError: PropTypes.bool,

    /**
     * A color string given in the format "#XXX" or "#XXXXXX". This option
     * determines the color that unsupported commands and invalid LaTeX are
     * rendered in when throwOnError is set to false. (default: #cc0000)
     */
    errorColor: PropTypes.string,

    /**
     *  A collection of custom macros. Each macro is a property with a name
     *  like \name (written "\\name" in JavaScript) which maps to a string
     *  that describes the expansion of the macro, or a function that accepts
     *  an instance of MacroExpander as first argument and returns the
     *  expansion as a string.
     */
    macros: PropTypes.string
};
